# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: QCDH · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hoá đơn token và tool chia số yêu cầu (274,7 đ); xem lại + làm lại chiếm 92,5% | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại +51,8% · tỉ lệ xem lại +40,7% · lương nhân viên +23,1% [simulated]; giá token chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | noi_dia 2.696 đ (0,22 lần), hang_nang 8.221 đ (0,69 lần), doi_tac 10.215 đ (0,85 lần), quoc_te 22.515 đ (1,88 lần so với 12.000 đ) [simulated]; thêm chi phí cố định: 4.599 đ (0,38 lần) ở 45.000 yêu cầu/tháng | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 4,25% (51/1.200); chưa có đối chứng nên chưa kết luận tác động; 8 event có `trace_id` | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 19/20 = 95%; 5 ca đủ 5 loại, mỗi ca có ngưỡng đo được và vai trò phụ trách | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, 859 mẫu mỗi nhóm, hệ số thiết kế 6,96, mức chênh 6 điểm; power còn 0,64 nếu tác động thật là 5 điểm; 3 luật dừng; quyết định 2027-01-05 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ [simulated]; xem lại 100%: 11.743 đ = 0,98 lần (12.415 đ = 1,03 lần) [simulated]; nửa khối lượng: +1.185 đ mỗi việc [simulated] | Giả lập | Trưởng nhóm CSKH |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

**Go có điều kiện** cho pilot chỉ ở `noi_dia` + `hang_nang` (quoc_te và doi_tac chuyển nhân viên). Con số bất lợi: nếu phải xem lại 100% thì chi phí là 0,98 lần chi phí nhân viên tự làm [simulated], không còn tiết kiệm; mức chênh 6 điểm chỉ có power 0,64 nếu tác động thật là 5 điểm. Điều kiện:

1. Sửa khoá chống trùng và đối soát sổ cái với API trả 503 (ca 7, 20) trước ngày bắt đầu; Kỹ sư trưởng agent; kiểm tra 2026-12-04.
2. Giám đốc vận hành ký chấp nhận mức chênh 6 điểm (power 0,64 ở mức 5 điểm); kiểm tra 2026-12-04.
3. Bật đủ 8 event có `trace_id` và thay phút `_simulated` bằng phút đo thật sau tuần 1; Trưởng nhóm CSKH; kiểm tra 2026-12-14.
4. Có kế hoạch giảm xem lại theo bậc (xem lại 100% thì không tiết kiệm, ngưỡng hoà vốn khoảng 4,8 đến 5,1 phút mỗi lần xem); PM trợ lý hoàn phí; kiểm tra 2026-12-14.
