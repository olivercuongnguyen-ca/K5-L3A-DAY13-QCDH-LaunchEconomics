# Báo cáo cá nhân — NguyenKhanhDuy-2A202603575

## 1. Thông tin thành viên

- Họ tên: Nguyễn Khánh Duy
- MSSV: 2A202603575
- Email: duynguyen77621@gmail.com
- GitHub: ZuyNoNguyen
- Nhóm / Lớp: QCDH / K5-L3A
- Vai trong nhóm: **Người kiểm số** (CP1, CP2 và rà soát đối chiếu số liệu CP5).

## 2. Phần việc phụ trách

- Phối hợp cùng Người viết code (thành viên H) đảm nhận **CP1 (Mô hình chi phí)** và **CP2 (Bảng độ nhạy)**.
- Kiểm tra chéo các phép tính từ `src/lab13.py` so với công thức gốc, bảo đảm không có sai số vượt 2%, mọi số từ cột `_simulated` đều có nhãn `simulated`, và mọi câu trả lời phân tích đều $\le 3$ dòng có số liệu.
- Điền hoàn thiện file `report/team/bang_chi_phi.md`.
- Rà soát tính nhất quán số liệu và event tracking giữa CP1–CP4 với **CP5** (`chi_so.md`, `ho_so_launch_v0.md`, `pilot_plan.yaml`) trước phiên duyệt chéo Gate 2a.

## 3. Đóng góp cụ thể

- **CP1 (`report/team/bang_chi_phi.md`, mục A1–A4):**
  - Kiểm chứng 3 phép thử A1 đạt (`1,20 · 1,25 · 1,25`).
  - Lập bảng A2 từ trace: Token `245.585 đ`, Tool `84.000 đ` (lần chạy 2 & 3 là `93.804 đ`), Xem lại `1.780.000 đ [simulated]`, Làm lại `2.264.000 đ [simulated]`, Tổng `4.373.585 đ`, 978 việc thành công, CPS `4.472 đ [simulated]` (gấp **16,3 lần** hoá đơn token+tool `274,7 đ/yc`; giờ nhân viên chiếm **92,5%**).
  - Phân tích A3 theo 4 loại yêu cầu (`noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, `quoc_te` 1,88× `[simulated]`) và chỉ rõ lý do `quoc_te` không nên chạy lại 3 lần (tỉ lệ `ok` giảm từ 30,0% $\to$ 11,4% $\to$ 2,2%).
  - Tính A4 phân bổ chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia + hang_nang`: `4.599 đ (0,38×)` ở 45.000 yc/tháng và `5.784 đ (0,48×)` khi giảm nửa khối lượng `[simulated]`.
- **CP2 (`report/team/bang_chi_phi.md`, mục B1–B4):**
  - Hoàn thiện 9 kịch bản độ nhạy B1, kiểm tra tính cộng tuyến tính B2 (Token x2 + Xem lại x2 = `6.543 đ`, `+46,3%`), xếp hạng 3 yếu tố nhạy nhất: `1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương nhân viên (+23,1%)`.
  - Đối chiếu B3: Chứng minh giới hạn 2 lần chạy rẻ nhất toàn hệ thống (`6.901.220 đ [simulated]`), khác với giới hạn 1 lần có CPS thấp nhất (`4.111 đ`) vì giới hạn 1 lần đẩy thêm 85 ca sang nhân viên.
  - Phân tích B4: Khi xem lại 100%, CPS lên `11.743 đ (0,98×)` với 9 phút làm lại hoặc `12.415 đ (1,03×)` với dữ liệu thực tế `15,3 phút/ca [simulated]`, chỉ ra ngưỡng hoà vốn xem lại $\le 4,8\text{–}5,1$ phút.
- **CP5 (`report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/pilot_plan.yaml`):**
  - Rà soát và khắc phục 3 lỗ hổng liên kết: bổ sung 2 event còn thiếu (`staff_rework_completed`, `handoff_to_staff`) vào `chi_so.md` để đủ **10 event có `trace_id`**, chỉnh lại diễn giải chi phí cố định nửa khối lượng ở Mục 7 (`2.370 đ/việc`, tổng `5.784 đ = 0,48×`), và bổ sung giới hạn 2 lần chạy/yêu cầu vào Điều kiện 1 của `ho_so_launch_v0.md`, đồng bộ tên vai trò `PM trợ lý hoàn phí` trong `pilot_plan.yaml`.

## 4. Bằng chứng

- **Git commits:**
  - `ce165fe` — *Update bang_chi_phi.md* (ZuyNoNguyen).
  - `eef9936` — *Update/CP5* (ZuyNoNguyen).
  - `f44e26a` — *Merge branch 'main'* (ZuyNoNguyen).
- **Files đóng góp:**
  - [report/team/bang_chi_phi.md](bang_chi_phi.md)
  - [report/team/chi_so.md](chi_so.md)
  - [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md)
  - [report/team/pilot_plan.yaml](pilot_plan.yaml)

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI trong IDE (Antigravity).
- **Mục đích sử dụng:**
  - Hỗ trợ kiểm tra chéo công thức, đối chiếu kết quả chạy `src/lab13.py` để điền nhanh và chuẩn xác vào `report/team/bang_chi_phi.md`.
  - Rà soát lỗ hổng logic giữa `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md` và `ho_so_launch_v0.md` theo Rubric 30 điểm Hội đồng.
- **Cách tự kiểm tra kết quả:**
  - Tự chạy lại `python lab13.py` trong `src/` để đối chiếu từng con số xuất ra màn hình với bảng trong `bang_chi_phi.md`.
  - Chạy lệnh Python kiểm tra `yaml.safe_load` trên `pilot_plan.yaml` và quét từ cấm `"production"` trên toàn bộ thư mục `report/team/`.

## 6. Tự đánh giá

- Hoàn thành tốt vai trò **Người kiểm số**, đảm bảo phần định giá kinh tế (CP1 & CP2) đạt độ chính xác 100% và không bị mất điểm trình bày/nhãn `simulated`.
- Chủ động kiểm tra chéo sang CP5 giúp hồ sơ Gate 2a của nhóm kín kẽ về mặt số liệu, nhất quán giữa bảng chi phí, bảng lỗi và danh sách event tracking trước giờ duyệt chéo 17:00.
