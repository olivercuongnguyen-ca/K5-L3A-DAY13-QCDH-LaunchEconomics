# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: QCDH
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu hỏi cho trợ lý hoàn phí LogiX-VN: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra quyết định. Dữ liệu là mẫu 1.200 yêu cầu (1.624 lần chạy), toàn bộ giả lập. Nhóm chia bốn vai (viết code, kiểm số, gắn nhãn 1, gắn nhãn 2 kiêm giữ hồ sơ) và đổi người viết code sau giờ giải lao.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **A (mô hình chi phí):** `src/lab13.py` tính chi phí mỗi việc thành công từ trace; tử số tính mọi lần chạy, mẫu số chỉ đếm 978 việc `thanh_cong`. Bảng A2–A4 trong [bang_chi_phi.md](bang_chi_phi.md).
- **B (độ nhạy):** 9 kịch bản, kịch bản cặp, giới hạn 1/2/3 lần chạy và xem lại 100% (B1–B4) trong [bang_chi_phi.md](bang_chi_phi.md).
- **C (bảng lỗi):** hai người gắn nhãn độc lập 20 ca, đồng thuận 19/20, bảng khắc phục 5 ca đủ 5 loại trong [bang_loi.md](bang_loi.md).
- **D (pilot):** cỡ mẫu và kế hoạch chia theo nhân viên 20 + 20 trong [pilot_plan.yaml](pilot_plan.yaml).
- **E (chỉ số, rủi ro, hồ sơ):** [chi_so.md](chi_so.md) và [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- Chi phí mỗi việc thành công **4.472 đ [simulated]**, gấp 16,3 lần hoá đơn token và tool chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5%.
- Ba yếu tố nhạy nhất [simulated]: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%).
- Theo loại: `noi_dia` 0,22 lần, `hang_nang` 0,69 lần, `doi_tac` 0,85 lần, `quoc_te` 1,88 lần so với 12.000 đ [simulated]; chạy lại 3 lần không cứu được `quoc_te` (30,0% → 11,4% → 2,2%).
- Pilot: chia theo nhân viên 20 + 20, 859 mẫu mỗi nhóm, mức chênh 6 điểm; power còn 0,64 nếu tác động thật là 5 điểm.
- **Đề xuất: Go có điều kiện**, chỉ cho `noi_dia` + `hang_nang`. Con số bất lợi: xem lại 100% ≈ 0,98 lần chi phí nhân viên tự làm [simulated].
- Kết quả duyệt chéo từ hội đồng: (điền sau buổi duyệt chéo).

## 5. Khó khăn và cách xử lý

- Ca 8 khiến hai người gắn nhãn lệch nhau (`Ngầm` và `Hệ thống`); nhóm thống nhất `Hệ thống` vì lỗi đã lộ trong tin nhắn gửi khách, và ghi quy tắc phân biệt trong `bang_loi.md`.
- Chia theo nhân viên 20 + 20 không đủ mẫu cho mức chênh 5 điểm; nhóm chấp nhận mức 6 điểm và ghi rõ power 0,64.
- Ngưỡng an toàn tuyệt đối 3% thấp hơn tỉ lệ mở lại hiện tại (4,25%); đổi sang +2 điểm so với đối chứng kèm trần 6%.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Mọi số tiền xem lại và làm lại là giả lập (`_simulated`); cần thay bằng số đo thật sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng, nên chỉ viết "chỉ số trong đợt chạy thử là…", không kết luận trợ lý đã nâng chỉ số.
- Chủ sở hữu pilot, ngày quyết định và ngày kiểm tra điều kiện là giả định của nhóm.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu statsmodels, lớp `NormalIndPower`
