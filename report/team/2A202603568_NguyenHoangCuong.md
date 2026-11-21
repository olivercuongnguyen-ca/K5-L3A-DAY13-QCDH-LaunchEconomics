# Báo cáo cá nhân — NguyenHoangCuong-2A202603568

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hoàng Cương
- MSSV: 2A202603568
- Email: (điền)
- GitHub: (điền)
- Nhóm / Lớp: QCDH / K5-L3A
- Vai trong nhóm: **Người gắn nhãn 2 kiêm giữ hồ sơ** (gắn nhãn độc lập 20 ca lỗi ở CP3; viết phần CP4 trong `src/lab13.py` sau giờ giải lao; điền `chi_so.md` và `ho_so_launch_v0.md` ở CP5).

## 2. Phần việc phụ trách

- **CP3 (Nhiệm vụ C):** gắn nhãn độc lập 20 ca lỗi theo năm loại Google PAIR, theo nguyên nhân gốc, không trao đổi với người gắn nhãn 1; soạn bản nháp bảng khắc phục cho 5 ca.
- **CP4 (Nhiệm vụ D):** viết hàm `chay_nhiem_vu_d` trong `src/lab13.py` (cỡ mẫu D1, tỉ lệ `mo_lai_trong_7_ngay`) và điền `report/team/pilot_plan.yaml`.
- **CP5 (Nhiệm vụ E):** điền `report/team/chi_so.md` và `report/team/ho_so_launch_v0.md`.

## 3. Đóng góp cụ thể

- **CP3:** bộ nhãn độc lập của tôi khác người 1 ở một ca (ca 8: tôi gắn `Ngầm`, người 1 gắn `Hệ thống`); nhóm thống nhất `Hệ thống`, đồng thuận 19/20 = 95%. Các ca tôi thấy dễ lệch khác là 13, 18 và 2.
- **CP4 (`src/lab13.py`):** a) 1.250 yêu cầu mỗi nhóm; b) hệ số thiết kế 2,48, 3.099 mỗi nhóm, 83 nhân viên > 40 nên không đủ người; c) tối đa 1.000 < 1.250; d) tối đa 300; e) m ≥ 299 yêu cầu mỗi nhân viên (dùng 859 do đề cho). Chọn chia theo nhân viên 20 + 20, mức chênh 6 điểm, power còn 0,64 nếu tác động thật là 5 điểm. Tỉ lệ mở lại hiện tại 4,25% (51/1.200), trong phạm vi 3,97% (39/982), nên ngưỡng an toàn là +2 điểm so với đối chứng hoặc trần 6%, không dùng ngưỡng tuyệt đối 3%.
- **CP5:** ba chỉ số tính thử (82,83% · 27,12% · 4,25%), 8 event có `trace_id`, 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy, hồ sơ 7 mục với đề xuất **Go có điều kiện** cho `noi_dia` + `hang_nang`, kèm các con số bất lợi (xem lại 100% = 0,98 lần chi phí nhân viên [simulated]; power 0,64).

## 4. Bằng chứng

- Commit `af6a3ae` (CP3 - labeler 2), `21ffbe4` (CP4), `ee27f82` (CP5), tác giả Hoang Cuong Nguyen.
- `python lab13.py` trong `src/` in ba phép thử ĐẠT và các số D1 ở trên; `yaml.safe_load` đọc được `pilot_plan.yaml`; không còn dấu `?` ngoài dòng chú thích; quét từ cấm trong `report/team` không có kết quả.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code.
- **Mục đích:** gợi ý nhãn và bản nháp bảng khắc phục CP3, viết hàm `chay_nhiem_vu_d`, soạn bản nháp `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`.
- **Cách tự kiểm tra:** nhãn CP3 gắn trước khi xem đáp án và không sửa sau khi so; chạy lại `lab13.py` và đối chiếu từng số D1 với hướng dẫn (lệch không quá 2%); tự kiểm `yaml.safe_load`, dấu `?`, từ cấm; đối chiếu số trong hồ sơ với `bang_chi_phi.md`. Cần tự giải thích được vì sao chia theo nhân viên 20 + 20 chỉ đạt 6 điểm.

## 6. Tự đánh giá

- Hoàn thành phần gắn nhãn, cỡ mẫu và hồ sơ launch v0; số liệu khớp đáp án trong ngưỡng 2%.
- Hạn chế: ngày quyết định, chủ sở hữu pilot và ngày kiểm tra điều kiện là giả định của nhóm; mọi số từ cột `_simulated` cần thay bằng số đo thật sau tuần 1 của pilot.
