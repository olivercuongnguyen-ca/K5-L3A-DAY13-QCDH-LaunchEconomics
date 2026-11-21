"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    if k is None:
        return 1.0 / p
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    if k is None:
        return 1.0
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công), hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong > 0 else float('nan')
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs) if len(reqs) > 0 else float('nan')

    return dict(
        token=float(tien_token.sum()),
        tool=float(tien_tool.sum()),
        chay_lai=float((tien_token + tien_tool)[runs['attempt'] > 1].sum()),
        xem_lai=float(xem_lai),
        lam_lai=float(lam_lai),
        tong=float(tong),
        thanh_cong=thanh_cong,
        cps=float(cps),
        hoa_don_moi_yc=float(hoa_don_moi_yc),
    )


def in_chi_tiet_a2(runs, reqs, ket_qua):
    """In chi tiết A2 phục vụ điền bảng và trả lời câu hỏi."""
    so_tool = int(runs['tool_calls'].sum())
    phut_xem = reqs['phut_xem_lai_simulated'].sum()
    phut_lam = reqs['phut_lam_lai_simulated'].sum()
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_so_gap = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    ti_trong_lam_lai = ket_qua['lam_lai'] / ket_qua['tong'] * 100
    ti_trong_xem_lai = ket_qua['xem_lai'] / ket_qua['tong'] * 100
    chi_phi_he_thong_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)

    print('\n=== A2 · CHI TIẾT MÔ HÌNH CHI PHÍ ===')
    print(f'So tool calls:            {so_tool:,}')
    print(f'Phut xem lai [sim]:       {phut_xem:,.1f}')
    print(f'Phut lam lai [sim]:       {phut_lam:,.1f}')
    print(f'Hoa don / yeu cau:        {ket_qua["hoa_don_moi_yc"]:,.1f} d')
    print(f'CPS [sim]:                {ket_qua["cps"]:,.0f} d (gap {he_so_gap:.1f}x hoa don)')
    print(f'Ti trong lam lai [sim]:   {ti_trong_lam_lai:.1f}%')
    print(f'Ti trong xem lai [sim]:   {ti_trong_xem_lai:.1f}%')
    print(f'Chi phi he thong / yc:    {chi_phi_he_thong_yc:,.0f} d ({chi_phi_he_thong_yc / BASELINE:.2f}x cua {BASELINE:,} d, {khong_tc} ca khong thanh cong)')


def chay_nhiem_vu_a3(runs, reqs):
    """Nhiệm vụ A3: tách chi phí theo từng loại yêu cầu và tỉ lệ ok theo attempt."""
    print('\n=== A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    loai_list = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']
    print(f'{"Loai":10s} {"So YC":>6s} {"Thanh cong":>10s} {"Lan chay/YC":>11s} {"CPS [sim]":>12s} {"So 12k":>8s}')
    for loai in loai_list:
        sub_reqs = reqs[reqs['loai'] == loai]
        res = mo_hinh(runs, sub_reqs)
        ti_le_tc = res['thanh_cong'] / len(sub_reqs) * 100
        lan_chay_tb = sub_reqs['so_lan_chay'].mean()
        print(f'{loai:10s} {len(sub_reqs):>6d} {ti_le_tc:>9.1f}% {lan_chay_tb:>11.2f} {res["cps"]:>11,.0f}d {res["cps"] / BASELINE:>7.2f}x')

    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(float)
    pivot_ok = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print('\nTi le status == ok theo tung lan thu (%):')
    print(pivot_ok.reindex(loai_list).round(1).to_string())


def chay_nhiem_vu_a4(runs, reqs, chi_phi_co_dinh_thang=40_000_000):
    """Nhiệm vụ A4: cộng chi phí cố định cho phạm vi noi_dia + hang_nang."""
    print('\n=== A4 · CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang) ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    res_pv = mo_hinh(runs, pham_vi)
    ti_le_tc_mau = res_pv['thanh_cong'] / len(reqs)
    print(f'Trong mau: {res_pv["thanh_cong"]}/{len(reqs)} ({ti_le_tc_mau * 100:.2f}%), CPS chua co dinh [sim]: {res_pv["cps"]:,.0f} d')

    for ten, khoi_luong in [('45.000 yc/thang', 45_000), ('Mot nua (22.500 yc/thang)', 22_500)]:
        viec_tc_thang = khoi_luong * ti_le_tc_mau
        co_dinh_viec = chi_phi_co_dinh_thang / viec_tc_thang
        tong_cps = res_pv['cps'] + co_dinh_viec
        print(f'{ten:26s} | VC/thang: {viec_tc_thang:>7,.0f} | Co dinh/viec: {co_dinh_viec:>6,.0f} d | Tong CPS [sim]: {tong_cps:>6,.0f} d ({tong_cps / BASELINE:.2f}x)')


def chay_nhiem_vu_b(runs, reqs):
    """Nhiệm vụ B: bảng độ nhạy (B1, B2), giới hạn chạy lại (B3), xem lại 100% (B4)."""
    print('\n=== B1 · BẢNG ĐỘ NHẠY ===')
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Gia token gap doi':      dict(gia_vao=52, gia_ra=260),
        'Gia token giam mot nua': dict(gia_vao=13, gia_ra=65),
        'Xem lai gap doi':        dict(he_so_xem_lai=2.0),
        'Xem lai giam mot nua':   dict(he_so_xem_lai=0.5),
        'Lam lai gap doi':        dict(he_so_lam_lai=2.0),
        'Lam lai giam mot nua':   dict(he_so_lam_lai=0.5),
        'Luong tang 25%':         dict(luong_phut=2500),
        'Toi da 2 lan chay':      dict(max_lan_chay=2),
        'Chi 1 lan chay':         dict(max_lan_chay=1),
    }
    print(f'{"Kich ban":25s} {"CPS [sim]":>12s} {"Thay doi":>10s}')
    print(f'{"Goc (A2)":25s} {goc:>11,.0f}d {"0.0%":>10s}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / goc - 1) * 100
        print(f'{ten:25s} {cps:>11,.0f}d {pct:>+9.1f}%')

    print('\n=== B2 · ĐỔI MỘT CẶP VÀ XẾP HẠNG ===')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f'Gia token x2 + Xem lai x2: {cap:,.0f} d ({(cap / goc - 1) * 100:+.1f}%) [sim]')

    print('\n=== B3 · GIỚI HẠN CHẠY LẠI VÀ CHI PHÍ CẢ HỆ THỐNG ===')
    print(f'{"Gioi han":10s} {"Tong tro ly [sim]":>18s} {"Khong TC":>10s} {"Ca he thong [sim]":>18s} {"CPS [sim]":>12s}')
    for k in [1, 2, 3]:
        res = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - res['thanh_cong']
        he_thong = res['tong'] + khong_tc * BASELINE
        print(f'{f"{k} lan":10s} {res["tong"]:>17,.0f}d {khong_tc:>10d} {he_thong:>17,.0f}d {res["cps"]:>11,.0f}d')

    print('\n=== B4 · NẾU PHẢI XEM LẠI TẤT CẢ (noi_dia + hang_nang) ===')
    pv_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pv_runs = runs[runs['request_id'].isin(pv_reqs['request_id'])]
    so_ok = pv_runs[pv_runs['status'] == 'ok']['request_id'].nunique()
    so_lam_lai = int((pv_reqs['ket_qua'] == 'lam_lai').sum())
    thanh_cong_pv = int((pv_reqs['ket_qua'] == 'thanh_cong').sum())
    chi_phi_ai_pv = (pv_runs['tokens_in'] / 1000 * GIA_VAO + pv_runs['tokens_out'] / 1000 * GIA_RA + pv_runs['tool_calls'] * GIA_TOOL).sum()

    all_rework = reqs[reqs['ket_qua'] == 'lam_lai']['phut_lam_lai_simulated']
    tb_lam_lai = all_rework.mean()
    tv_lam_lai = all_rework.median()
    print(f'Yeu cau co it nhat 1 run ok: {so_ok} | Ca lam_lai: {so_lam_lai} | Thanh cong: {thanh_cong_pv} | Token+Tool: {chi_phi_ai_pv:,.0f} d')
    print(f'Phut lam lai thuc te [sim] (toan bo ca lam_lai): TB = {tb_lam_lai:.2f} phut, Trung vi = {tv_lam_lai:.1f} phut')

    for nhan, phut_ll in [('De bai (9 phut/ca)', 9.0), (f'Du lieu thuc ({tb_lam_lai:.1f} phut/ca)', tb_lam_lai)]:
        tien_xem = so_ok * 5 * LUONG_PHUT
        tien_lam = so_lam_lai * phut_ll * LUONG_PHUT
        tong_b4 = chi_phi_ai_pv + tien_xem + tien_lam
        cps_b4 = tong_b4 / thanh_cong_pv
        hoa_von = (thanh_cong_pv * BASELINE - chi_phi_ai_pv - tien_lam) / (so_ok * LUONG_PHUT)
        print(f'{nhan:35s} -> Tong: {tong_b4:>10,.0f} d | CPS [sim]: {cps_b4:>6,.0f} d ({cps_b4 / BASELINE:.2f}x) | Hoa von xem lai <= {hoa_von:.1f} phut')


def chay_nhiem_vu_d(reqs):
    """Nhiem vu D: co mau (D1) va ty le mo lai hien tai (D3)."""
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower
    ICC, ALPHA, POWER = 0.02, 0.05, 0.8

    def co_mau(p1, p2):
        es = proportion_effectsize(p2, p1)
        return NormalIndPower().solve_power(es, alpha=ALPHA, power=POWER, ratio=1.0)

    print('\n=== D1 · Co mau (baseline 0,70; alpha 0,05; power 0,8; ICC 0,02) ===')
    n_a = co_mau(0.70, 0.75)
    print(f'a) Chia theo yeu cau, +5 diem: {n_a:,.0f} moi nhom')
    de_b = 1 + (75 - 1) * ICC
    n_b = n_a * de_b
    print(f'b) m=75: DE={de_b:.2f}; n={n_b:,.0f} moi nhom; {n_b / 75:.1f} nhan vien/nhom, tong {2 * n_b / 75:.0f} (co 40)')
    print(f'c) 20 nhan vien/nhom: toi da {20 / ICC:,.0f} < {n_a:,.0f}: {"dat" if 20 / ICC >= n_a else "khong dat"}')
    print(f'd) 6 depot/nhom: toi da {6 / ICC:,.0f}')
    n6 = 859  # de bai cho san (statsmodels ra ~857)
    m_e = math.ceil(n6 * (1 - ICC) / (20 - n6 * ICC))
    print(f'e) +6 diem: n={n6:,.0f}; m >= {m_e} yeu cau/nguoi (DE {1 + (m_e - 1) * ICC:.2f})')
    es = proportion_effectsize(0.75, 0.70)
    print(f'   power neu thuc te +5 diem, n=859: {NormalIndPower().power(es, nobs1=859, alpha=ALPHA):.2f}')

    print('\n=== D3 · Ty le mo lai trong 7 ngay ===')
    print(f'Toan mau: {reqs.mo_lai_trong_7_ngay.mean():.2%} ({int(reqs.mo_lai_trong_7_ngay.sum())}/{len(reqs)})')
    pv = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    print(f'noi_dia + hang_nang: {pv.mo_lai_trong_7_ngay.mean():.2%} ({int(pv.mo_lai_trong_7_ngay.sum())}/{len(pv)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    in_chi_tiet_a2(runs, reqs, ket_qua)
    chay_nhiem_vu_a3(runs, reqs)
    chay_nhiem_vu_a4(runs, reqs)
    chay_nhiem_vu_b(runs, reqs)
    chay_nhiem_vu_d(reqs)
