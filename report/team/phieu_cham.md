# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): QCDH
- Nhóm được chấm: Armless

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | "Go có điều kiện" khớp số của nhóm. Hồ sơ nêu rõ số bất lợi: power chỉ ≈ 0,64 nếu tác động thật là +5 điểm (đã chấp nhận MDE 6 điểm); xem lại 100% làm chi phí lên 11.743–12.415 đ/việc (0,98–1,03× mốc 12.000 đ) [simulated]. Cách xử lý có người phụ trách và ngày kiểm tra (văn bản chấp nhận MDE, diễn tập cờ tắt 30 phút, giảm xem lại dưới 50% cuối bậc 25%, quyết định 05/01/2027). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 9 | Hầu hết số chi phí đều gắn `[simulated]` (4.472 đ, 6.787 đ, 3.414 đ, 11.743 đ…). Phạm vi thu hẹp về `noi_dia` + `hang_nang` có lý do bằng số: `quoc_te` thành công 27,3%, tốn 2,32 lần chạy/yêu cầu, 22.515 đ/việc (1,88× nhân viên). Trừ 1 điểm: các số E1 trong mục 4 của hồ sơ (82,83%, 27,12%, 4,25%) chỉ có chú thích chung ở đầu, không gắn nhãn ngay trên từng con số. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 8 | Tách được tác động: đối chứng chạy đồng thời, bốc thăm bằng code theo nhân viên, 20 cụm mỗi nhóm, cỡ mẫu 859 hiệu dụng/nhóm (DE = 6,96; m ≥ 299 yêu cầu/người). 4 luật dừng có ngưỡng, thời hạn và người quyết định (ví dụ: mở lại chênh ≥ 2 điểm hoặc ≥ 6%, 1 ca hoàn trùng thì Giám đốc vận hành bật cờ tắt trong 30 phút). Trừ 2 điểm vì không nhất quán: `assignment.unit` là nhân viên (4 → 10 → 20 người) nhưng phần định nghĩa luật dừng nói chia ngẫu nhiên theo yêu cầu; baseline 0,70 trong cỡ mẫu so với 91,6% (900/982) thành công trong phạm vi; luật chi phí 8.000 đ chưa nói rõ tỉ lệ xem lại mà mốc 3.414 đ giả định (128/982 ≈ 13%, trong khi B4 dùng 948/982 ≈ 97%). |
| **Tổng** | | | | **27 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Đề xuất khớp số của chính nhóm và nêu rõ cả hai con số bất lợi (power ≈ 0,64 nếu tác động +5 điểm; chi phí 11.743–12.415 đ/việc nếu xem lại 100%). Phạm vi chỉ gồm `noi_dia` (95,0% thành công, 2.696 đ/việc) và `hang_nang` (74,1%, 8.221 đ/việc), loại `quoc_te` (27,3%, 22.515 đ/việc) [simulated]. Pilot có đối chứng đồng thời và 4 luật dừng đủ ngưỡng, thời hạn, người dừng. Điều kiện của hội đồng: trước ngày bắt đầu, nhóm làm rõ đơn vị chia ngẫu nhiên (nhân viên hay yêu cầu), tỉ lệ xem lại ban đầu, và baseline của chỉ số chính trong phạm vi.

**Một câu hỏi cho đội trình:** Mốc 3.414 đ/việc của đợt chạy thử giả định bao nhiêu phần trăm yêu cầu được xem lại? Hồ sơ ghi 128 ca xem lại trên 982 yêu cầu (≈13%), còn B4 tính 948/982 (≈97%) và ra 11.743–12.415 đ. Nếu pilot chạy ở mức xem lại gần B4, chi phí gộp vượt 8.000 đ, luật dừng #2 có kích hoạt sau tuần thứ 2 không? Nhóm dự kiến xem lại ở mức nào ở bậc rollout 10%?

**Câu trả lời của đội trình (ghi lại tại buổi):** Mốc 3.414 đ ứng với mức xem lại 13% (128/982). B4 thì xem lại 96,5% (948/982). Ở mức đó chi phí khoảng 11.700–12.400 đ, nên luật #2 sẽ kích hoạt. Vì chi phí phải đợi 7 ngày theo dõi mới tính được, luật kích hoạt vào đầu tuần 4, khi pilot đã ở bậc 50%. Hành động "bỏ hang_nang" lúc đó vừa không đưa chi phí về dưới 8.000 đ, vừa làm hỏng phép đo chỉ số chính. Nhóm sửa như sau:

Ghi rõ tỉ lệ xem lại cho từng bậc: 10% → 100%, 25% → 100%, 50% → dưới 50%.
Đặt ngưỡng chi phí theo tỉ lệ xem lại: 12.000 đ khi xem lại từ 50% trở lên, 8.000 đ khi dưới 50%. Ngưỡng 8.000 đ ứng với mức xem lại khoảng 55%.
Trong giai đoạn đo chỉ số chính, đổi hành động "bỏ hang_nang" thành "giữ nguyên bậc rollout".