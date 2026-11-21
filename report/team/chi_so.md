# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhân viên nhóm trợ lý được mở bằng trợ lý | Số yêu cầu có `agent_suggestion_shown` chia số yêu cầu của nhân viên nhóm trợ lý (`refund_request_created`) | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | `so_tien_da_hoan` khác `so_tien_dung` trong 100 đơn mẫu, chia 100 | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi bấm gửi, sửa hoặc bỏ |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, ly_do, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `refund_request_created` (mốc bắt đầu) + `ticket_closed` (trong 24 giờ) − `ticket_reopened` (trong 7 ngày).
- Chỉ số dùng (bỏ qua gợi ý): `staff_review_decision` với `quyet_dinh` là sửa hoặc bỏ, chia số `staff_review_decision`.
- Chỉ số dùng tự đề xuất (% mở bằng trợ lý): `agent_suggestion_shown` chia `refund_request_created` của nhóm trợ lý.
- Chỉ số an toàn: `ticket_reopened` chia `refund_request_created`.
- Chỉ số an toàn tự đề xuất: `audit_sample_checked`; cả năm chỉ số đều tính được từ danh sách event, nối bằng `trace_id`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại gấp đôi | +51,8%, chi phí mỗi việc thành công lên 6.787 đ [simulated] (từ 4.472 đ) | Tỉ lệ `lam_lai` theo tuần trên 7% (đợt chạy thử: 4,9% trong noi_dia + hang_nang, 48/982) | Thu hẹp về `noi_dia`, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98 lần 12.000 đ [simulated]; 12.415 đ = 1,03 lần nếu làm lại 15,3 phút như trong dữ liệu [simulated] | % yêu cầu được xem lại còn trên 50% khi kết thúc bước rollout 0,25 (đợt chạy thử: 13,0% bị xem lại trong phạm vi) | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15% (hiện 27,1%) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ mỗi tháng: +1.185 đ mỗi việc ở 45.000 yêu cầu/tháng, +2.370 đ nếu còn một nửa [simulated] | Số việc thành công mỗi tuần dưới 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
