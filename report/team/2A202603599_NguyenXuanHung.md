# Báo cáo cá nhân — NguyenXuanHung-2A202603599

## 1. Thông tin thành viên

- Họ tên: Nguyễn Xuân Hùng
- MSSV: 2A202603599
- Email: xuanhung17032003@gmail.com
- GitHub: XuanHung1703
- Nhóm / Lớp: QCDH / K5-L3A
- Vai trong nhóm: **Người viết code** (viết và chạy `src/lab13.py` cho CP1 & CP2; chuyển giao vai viết code CP4 cho thành viên khác sau giờ giải lao; kiểm tra kỹ thuật và đối chiếu số liệu).

## 2. Phần việc phụ trách

- Triển khai phần code tính toán cho **Nhiệm vụ A (CP1)** và **Nhiệm vụ B (CP2)** trong `src/lab13.py`, bảo đảm đọc đúng `logix_runs.csv` và `logix_requests.csv` (`keep_default_na=False`) và xuất đủ bảng số liệu để **Người kiểm số** đối chiếu và điền vào `report/team/bang_chi_phi.md`.
- Phối hợp rà soát kỹ thuật sau khi nhóm hoàn thiện CP3–CP5: chạy lại `src/lab13.py`, kiểm tra cú pháp `report/team/pilot_plan.yaml` bằng `yaml.safe_load`, và kiểm tra các quy tắc liêm chính/nộp bài của lab.

## 3. Đóng góp cụ thể

- **CP1 (`src/lab13.py` — Nhiệm vụ A1–A4):**
  - Viết 3 hàm lý thuyết `so_lan_chay_ky_vong(p, k)`, `ti_le_thanh_cong(p, k)`, `he_so_chi_phi_moi_viec_thanh_cong(p, k)` vượt qua 3 phép thử bắt buộc trong `kiem_tra_dap_an_biet_truoc()` (`1,20 · 1,25 · 1,25`).
  - Viết hàm `mo_hinh(runs, reqs, ...)` tính đủ các khoản `token`, `tool`, `chay_lai` (`attempt > 1`), `xem_lai`, `lam_lai`, `tong`, `thanh_cong`, `cps`, `hoa_don_moi_yc` (CPS gốc `4.472 đ` `[simulated]`, gấp `16,3×` hoá đơn `274,7 đ`; chi phí cả hệ thống `5.865 đ/yc = 0,49×` của `12.000 đ`).
  - Viết `chay_nhiem_vu_a3` tách chi phí cho 4 loại (`noi_dia` `0,22×`, `hang_nang` `0,69×`, `doi_tac` `0,85×`, `quoc_te` `1,88×`) kèm bảng pivot tỉ lệ `status == 'ok'` theo từng `attempt` (1, 2, 3) chứng minh `quoc_te` chạy lại không hiệu quả (`30,0% → 11,4% → 2,2%`).
  - Viết `chay_nhiem_vu_a4` phân bổ chi phí cố định `40 triệu đ/tháng` cho phạm vi `noi_dia + hang_nang` (`4.599 đ = 0,38×` ở `45.000` yc/tháng và `5.784 đ = 0,48×` ở `22.500` yc/tháng).
- **CP2 (`src/lab13.py` — Nhiệm vụ B1–B4):**
  - Viết `chay_nhiem_vu_b` chạy đủ 9 kịch bản độ nhạy B1, kịch bản kết hợp B2 (`6.543 đ`, `+46,3%`), bảng chi phí cả hệ thống theo giới hạn `1, 2, 3` lần chạy B3 (chỉ ra giới hạn `2` lần rẻ nhất cho công ty: `6.901.220 đ`), và kịch bản xem lại `100%` B4 (cả mức đề bài 9 phút/ca `11.743 đ = 0,98×` lẫn mức thực tế từ dữ liệu `15,3` phút/ca `12.415 đ = 1,03×`, cùng ngưỡng hoà vốn `≤ 4,8–5,1` phút).
- **Kiểm tra chéo CP4–CP5:** Kiểm tra `yaml.safe_load` cho `report/team/pilot_plan.yaml`, kiểm tra không còn dấu `?` ngoài dòng chú thích `#`, và quét từ cấm trong `report/team/`.

## 4. Bằng chứng

- **Git commit:** `e664b31` — *feat(src): implement CP1 and CP2 in lab13.py* (tác giả `XuanHung1703 <xuanhung17032003@gmail.com>`), thêm `157` dòng vào `src/lab13.py`.
- **Kết quả chạy thực tế `python lab13.py` (trong `src/`):** In `Ba phép thử đáp án biết trước: ĐẠT` và toàn bộ bảng A2, A3, A4, B1, B2, B3, B4 khớp với số liệu trong `report/team/bang_chi_phi.md`.
- **Kiểm tra hợp lệ sau cập nhật của nhóm:** `python -c "import yaml; yaml.safe_load(open('report/team/pilot_plan.yaml', encoding='utf-8'))"` in `YAML OK`, không còn dấu `?` ngoài comment, và không có từ cấm trong `report/team/`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI trong IDE (Antigravity).
- **Mục đích sử dụng:**
  - Phân tích đề bài, tóm tắt yêu cầu cho vai trò **Người viết code**.
  - Hỗ trợ viết và chuẩn hoá code `src/lab13.py` cho CP1 & CP2, chạy lệnh kiểm tra `pilot_plan.yaml` và giải thích ý nghĩa các chỉ số kinh tế (`CPS`, chi phí cả hệ thống, độ nhạy, đánh đổi loại `doi_tac`/`quoc_te`).
- **Cách tự kiểm tra kết quả:**
  - Chạy trực tiếp `python lab13.py` trong `src/`, xác nhận 3 phép thử A1 in `ĐẠT` (`1,20 · 1,25 · 1,25`) và đối chiếu từng con số với tài liệu hướng dẫn cũng như phần kiểm tra của **Người kiểm số** trong `report/team/bang_chi_phi.md`.
  - Giữ nguyên file báo cáo `bang_chi_phi.md` để Người kiểm số tự đối chiếu và điền độc lập, rồi mới pull về kiểm tra chéo.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần việc của **Người viết code** ở nửa đầu buổi (CP1 & CP2), đảm bảo số liệu chạy ra chính xác, rõ ràng và tách biệt hoàn toàn với phần điền bảng của Người kiểm số.
- Thực hiện đúng quy định đổi người viết code sau giờ giải lao để thành viên khác tự tay viết phần CP4 (`chay_nhiem_vu_d`), đồng thời nắm được bản chất các con số trọng tâm (tỉ trọng `92,5%` giờ nhân viên, lý do chọn giới hạn `2` lần chạy, rủi ro xem lại `100%` và phạm vi `noi_dia + hang_nang`) để sẵn sàng bảo vệ trước hội đồng Gate 2a.
