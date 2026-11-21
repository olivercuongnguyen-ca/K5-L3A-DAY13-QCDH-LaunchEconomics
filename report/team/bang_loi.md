# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Thành viên gắn nhãn 1 · Người gắn nhãn 2: Thành viên gắn nhãn 2 (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 8 (`Hệ thống`, không phải `Ngầm`):** Trích dẫn sai "Điều 7.2" không tồn tại là lỗi **`Hệ thống`** vì nội dung sai đã lộ trực tiếp trong tin nhắn gửi khách, còn `Ngầm` chỉ dùng khi không ai nhận ra lỗi cho tới khi kiểm tra mẫu hoặc đối soát.

*(Ghi chú thêm ranh giới cho các ca dễ lệch mà hai người đã lưu ý để thống nhất khi bảo vệ):*

- **Ca 2 và Ca 15 (`Hệ thống`, không phải `Ngầm`):** Lỗi gọi sai tham số bảng giá (khách phát hiện mở lại) và tính sai 100% thay vì 50% (nhân viên xem lại bắt được) đều đã lộ ra trước hoặc ngay khi giao dịch diễn ra.
- **Ca 6 và Ca 9 (`Do người dùng`, không phải `Hệ thống`):** Gốc lỗi là khách chọn sai danh mục hoặc nhập sai mã sàn TMĐT thay vì mã vận đơn; việc chưa tự gợi ý nằm ở giải pháp khắc phục.
- **Ca 13 (`Giới hạn hệ thống`, không phải `Hệ thống`):** Bảo hiểm của đối tác nằm ngoài phạm vi trợ lý nên gốc lỗi là giới hạn hệ thống dù câu từ chối còn chung chung.
- **Ca 18 (`Ngữ cảnh`, không phải `Hệ thống`):** Số tiền 15.000 đ hoàn đúng chính sách 50%, lỗi phát sinh do giả định khách tự hiểu cách tính không khớp hoàn cảnh thực tế.
- **Ca 12 (`Ngầm`, không phải `Hệ thống`):** Kết quả vẫn đúng nhưng chi phí token depot D05 tăng gấp 3 lần suốt 3 tuần không ai thấy, cho thấy lỗi ngầm bao gồm cả sai lệch về chi phí.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` có `trace_id`; cảnh báo khi tỉ lệ vượt 2% tổng yêu cầu mỗi ngày | Nhận diện định dạng mã sàn TMĐT để tự tra chéo sang mã vận đơn LogiX; nếu không tra được thì hiển thị hướng dẫn kèm ảnh vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Job đối soát mỗi giờ theo `trace_id`: đếm số tin nhắn báo "đã hoàn" nhưng thiếu event `refund_ledger_write` trạng thái `ok`; ngưỡng cảnh báo > 0 ca | Chỉ cho phép gửi thông báo "đã hoàn tiền thành công" khi API sổ cái trả `ok`; nếu lỗi 503 sau 3 lần thử thì báo "đang xử lý" và tạo event `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tổng hợp hằng tuần event `ticket_reopened` có `trace_id` và lý do thắc mắc số tiền hoàn dù kiểm tra lại cho thấy tiền hoàn đúng; ngưỡng cảnh báo > 1% yêu cầu/tuần | Bổ sung phép tính cụ thể vào mẫu tin nhắn phản hồi (ví dụ: `30.000 đ × 50% = 15.000 đ`) để khách đối chiếu ngay | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` có `trace_id` và `reason = thieu_du_lieu_chang_ngoai`, thống kê hằng ngày theo cột `loai`; cảnh báo khi vượt 5% trong phạm vi pilot | Duy trì luồng chuyển ngay cho nhân viên kèm bản tóm tắt ca; loại nhóm yêu cầu `quoc_te` ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` gắn `trace_id` khi kiểm tra mẫu 100 đơn ngẫu nhiên mỗi tuần so với bảng giá hiện hành; ngưỡng cảnh báo > 1% đơn lệch tiền | Tự động xoá bộ nhớ đệm khi có cập nhật bảng giá mới và ghi kèm mã phiên bản bảng giá vào từng `trace_id` | Kế toán trưởng |
