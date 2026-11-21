# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: (chờ điền) · Người gắn nhãn 2: (đã gắn xong, cột bên dưới) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ? (chờ người 1) | Do người dùng | ? | ? |
| 2 | ? (chờ người 1) | Hệ thống | ? | ? |
| 3 | ? (chờ người 1) | Ngữ cảnh | ? | ? |
| 4 | ? (chờ người 1) | Giới hạn hệ thống | ? | ? |
| 5 | ? (chờ người 1) | Ngầm | ? | ? |
| 6 | ? (chờ người 1) | Do người dùng | ? | ? |
| 7 | ? (chờ người 1) | Hệ thống | ? | ? |
| 8 | ? (chờ người 1) | Ngầm | ? | ? |
| 9 | ? (chờ người 1) | Do người dùng | ? | ? |
| 10 | ? (chờ người 1) | Ngữ cảnh | ? | ? |
| 11 | ? (chờ người 1) | Giới hạn hệ thống | ? | ? |
| 12 | ? (chờ người 1) | Ngầm | ? | ? |
| 13 | ? (chờ người 1) | Giới hạn hệ thống | ? | ? |
| 14 | ? (chờ người 1) | Do người dùng | ? | ? |
| 15 | ? (chờ người 1) | Hệ thống | ? | ? |
| 16 | ? (chờ người 1) | Ngữ cảnh | ? | ? |
| 17 | ? (chờ người 1) | Ngầm | ? | ? |
| 18 | ? (chờ người 1) | Ngữ cảnh | ? | ? |
| 19 | ? (chờ người 1) | Giới hạn hệ thống | ? | ? |
| 20 | ? (chờ người 1) | Hệ thống | ? | ? |

**Tỉ lệ đồng thuận:** ? / 20 = ?% (chờ bộ nhãn của người 1)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- (Điền sau khi so nhãn. Các ca người 2 thấy dễ lệch: 8 (Ngầm hay Hệ thống), 13 (Giới hạn hay Hệ thống), 18 (Ngữ cảnh hay Hệ thống), 2 (Hệ thống hay Ngầm).)

## Bảng khắc phục cho 5 ca, mỗi loại một ca

*Bản nháp của người gắn nhãn 2 theo nhãn riêng; kiểm lại sau khi thống nhất nhãn.*

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `intent_rejected` với lý do `invalid_order_id` > 5% số yêu cầu/tuần (theo dõi hằng tuần) | Dò định dạng mã vận đơn ngay lúc nhập; nếu giống mã sàn TMĐT thì gợi ý nơi tìm mã vận đơn thay vì chỉ báo lỗi | Quản lý sản phẩm trợ lý |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn “đã hoàn” không có bản ghi sổ cái ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo “đã hoàn” khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo “đang xử lý” và chuyển nhân viên | Kỹ sư trưởng agent |
| 10 | Ngữ cảnh | Tỉ lệ mở lại trong 7 ngày của đơn bị từ chối do bất khả kháng > 10%/tuần | Hiện cảnh báo bất khả kháng cạnh “cam kết 24 giờ” trong ứng dụng; trợ lý giải thích điều khoản khi từ chối | Quản lý vận hành CSKH |
| 19 | Giới hạn hệ thống | Event `out_of_data_window` đếm hằng tuần; theo dõi nếu > 2% yêu cầu | Giữ cách xử lý hiện tại (nói rõ + chuyển nhân viên kèm tóm tắt); nhân viên phản hồi trong 4 giờ làm việc | Trưởng nhóm CSKH |
| 17 | Ngầm | Kiểm tra mẫu hằng tuần 100 đơn so với bảng giá hiện hành; ngưỡng sai lệch > 1% đơn; thêm cảnh báo khi phiên bản bảng giá của cache khác bản gốc | Gắn phiên bản bảng giá vào cache, hết hạn khi bảng giá đổi; quét hoàn bù cho 212 đơn bị lệch | Kỹ sư dữ liệu |
