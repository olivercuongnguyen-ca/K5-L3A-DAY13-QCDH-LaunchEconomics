# Báo cáo cá nhân — VuTrongQuang-2A202603535

## 1. Thông tin thành viên

- Họ tên: Vũ Trọng Quang
- MSSV: 2A202603535
- Email: trongquangvu2004@gmail.com
- GitHub: Quangvu256
- Nhóm / Lớp: QCDH / K5-L3A
- Vai trong nhóm: **Người gắn nhãn 1** (đọc đề, theo dõi điều kiện "Xong khi" và kiểm soát chất lượng QA xuyên suốt CP1–CP5; gắn nhãn độc lập 20 ca lỗi ở CP3).

## 2. Phần việc phụ trách

- Theo dõi tiêu chí **"Xong khi"** và các quy tắc bắt buộc của lab ([RULES.md](../../RULES.md), [CHECKPOINTS.md](../../CHECKPOINTS.md), [RUBRIC.md](../../RUBRIC.md)) trên toàn bộ sản phẩm của nhóm: nhãn `simulated` cho các số từ cột `_simulated`, định dạng bảng khắc phục có `trace_id` và vai trò phụ trách đơn lẻ, không còn dấu `?` ngoài dòng chú thích trong `pilot_plan.yaml`, và không xuất hiện từ cấm.
- Phụ trách chính phía **Người gắn nhãn 1** trong **Nhiệm vụ C (CP3)**: đọc 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, gắn nhãn độc lập theo 5 loại Google PAIR dựa trên nguyên nhân gốc, đối chiếu với Người gắn nhãn 2, viết quy tắc phân biệt và hoàn thiện bảng khắc phục 5 ca.
- Kiểm tra chéo toàn bộ bộ hồ sơ `CP1`–`CP5` sau khi các thành viên hoàn thiện code và tài liệu trước phiên duyệt chéo Gate 2a.

## 3. Đóng góp cụ thể

- **CP1 & CP2 (`bang_chi_phi.md`, `src/lab13.py`):** Đọc đề, rà soát điều kiện hoàn thành và đối chiếu số đầu ra từ `src/lab13.py` (3 phép thử A1 `1,20 · 1,25 · 1,25` ĐẠT, bảng A2–A4, độ nhạy B1–B4), kiểm tra nhãn `simulated` và giới hạn độ dài `≤ 3 dòng/câu` trong `report/team/bang_chi_phi.md`.
- **CP3 (`report/team/bang_loi.md`):**
  - Gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc (`Do người dùng`: 1, 6, 9, 14; `Hệ thống`: 2, 7, 8, 15, 20; `Ngữ cảnh`: 3, 10, 16, 18; `Giới hạn hệ thống`: 4, 11, 13, 19; `Ngầm`: 5, 12, 17).
  - Xử lý merge conflict với commit `af6a3ae` (bộ nhãn độc lập của Người gắn nhãn 2), giữ nguyên vẹn cột nhãn độc lập của hai người trước khi so, tính tỉ lệ đồng thuận **`19 / 20 = 95%`**.
  - Thống nhất nhãn **Ca 8** (`Hệ thống`, không phải `Ngầm`), viết câu quy tắc phân biệt cho Ca 8 cùng ghi chú ranh giới cho các ca dễ nhầm (Ca 2, 6, 9, 12, 13, 15, 18), và hoàn thiện bảng khắc phục 5 ca đại diện đủ 5 loại (Ca 9, 7, 18, 4, 17) với event có `trace_id`, ngưỡng đo được và một vai trò phụ trách cụ thể.
- **CP4 & CP5 (`pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`):** Chạy kiểm chứng `src/lab13.py`, xác thực cấu trúc YAML (`yaml.safe_load`), kiểm tra 3 luật dừng 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`, kiểm tra 5 chỉ số E1, 8 event có `trace_id`, 3 dòng rủi ro kinh tế E2, và rà soát tính nhất quán số liệu trên 7 mục của `ho_so_launch_v0.md` trước phiên duyệt chéo Gate 2a.

## 4. Bằng chứng

- **Git commit:** `285b043` — *Merge CP3: gop nhan nguoi 1 va nguoi 2 (95%)* (tác giả `Quangvu256 <trongquangvu2004@gmail.com>`), giải quyết conflict và hợp nhất bộ nhãn CP3 trên nhánh `main`.
- **File [bang_loi.md](bang_loi.md):** Đủ 20 dòng nhãn độc lập của Người gắn nhãn 1 & 2, tỉ lệ đồng thuận `19 / 20 = 95%`, quy tắc phân biệt Ca 8 (`Hệ thống` vs `Ngầm`), và bảng khắc phục 5 ca (Ca 9, 7, 18, 4, 17).
- **Kiểm chứng kỹ thuật tự chạy:**
  - `python lab13.py` (trong `src/`): In `Ba phép thử đáp án biết trước: ĐẠT`, CPS chung `4.472 đ` `[simulated]` (gấp `16,3×` hoá đơn `274,7 đ`), D1 (`1.250` mẫu/nhóm; mức chênh 6 điểm `n=859`, `m >= 299`, `DE = 6,96`, power `0,64` ở mức 5 điểm), D3 (`mo_lai_trong_7_ngay`: `4,25%` toàn mẫu, `3,97%` trong `noi_dia + hang_nang`).
  - Kiểm tra `pilot_plan.yaml`: đọc hợp lệ bằng `yaml.safe_load`, `clusters_per_arm == 20`, không còn dấu `?` ngoài dòng `#`, không có từ cấm trong `report/team/`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI trong IDE (Antigravity).
- **Mục đích sử dụng:**
  - Tra cứu và đối chiếu phân loại 5 nhóm lỗi theo Google PAIR, các tiêu chí "Xong khi" và thang chấm Rubric của Lab 13.
  - Hỗ trợ so sánh hai bộ nhãn khi xảy ra Git merge conflict trên `report/team/bang_loi.md`, viết lệnh kiểm tra tự động cú pháp YAML, từ cấm và tính đầy đủ của bảng biểu.
  - Hỗ trợ soạn thảo cấu trúc báo cáo cá nhân từ bằng chứng thực tế trong repo.
- **Cách tự kiểm tra kết quả:**
  - Tự đọc mô tả 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và chốt bộ nhãn độc lập của Người gắn nhãn 1 theo nguyên nhân gốc trước khi gộp với commit `af6a3ae` của Người gắn nhãn 2.
  - Tự chạy lại `python lab13.py` trong thư mục `src/` và dùng script Python kiểm tra chéo các file trong `report/team/` (`bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`) với `CHECKPOINTS.md` và `RUBRIC.md`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ trách nhiệm của vai **Người gắn nhãn 1**, giữ đúng quy trình liêm chính của Lab 13 (gắn nhãn độc lập trước, không chỉnh sửa lại cột nhãn gốc sau khi đối chiếu với Người gắn nhãn 2).
- Thực hiện kiểm tra chéo xuyên suốt 5 checkpoint giúp phát hiện và bảo đảm các chi tiết dễ mất điểm hội đồng (nhãn `simulated`, `trace_id` trên mọi event/cách phát hiện lỗi, 1 vai trò phụ trách duy nhất, công bố thẳng con số bất lợi `power = 0,64` ở mức 5 điểm và chi phí xem lại 100% `0,98×`–`1,03×`).
- **Việc còn lại của nhóm sau khi nộp báo cáo cá nhân:** điền bảng thành viên vào `TEAM.md`, chấm chéo vào `report/team/phieu_cham.md` lúc 17:00, hoàn thiện `report/team/group_report.md` và push commit chốt trước deadline.
