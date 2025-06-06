"""Bias words utilised to compute the bias metrics.

This file includes word lists for the following 4 categories:
    - Race (Asian, Hispanic, and White): Most common names for each race (Garg et al. 2018)
    - Gender (Female, Male): Gender specific words - such as woman, man etc. - for each gender (Bolukbasi et al. 2016)
    - Adjectives: List of adjectives (Garg et al. 2018)
    - Professions: List of professions (Bolukbasi et al. 2016)

References:
    - Garg et al. 2018      | https://arxiv.org/abs/1711.08412
    - Bolukbasi et al. 2016 | https://arxiv.org/abs/1607.06520

"""

from typing import Dict, List


FEMALE_WORDS: List[str] = [
    "gái",
    "con gái",
    "cô gái",
    "chị gái",
    "em gái",
    "bạn gái",
    "cháu gái",
    "nữ hoàng",
    "nữ phục vụ",
    "mẹ",
    "mẹ kế",
    "bà",
    "mụ",
    "cô",
    "cô ấy",
    "dì",
    "chị",
    "chị ấy",
    "nàng",
    "phụ nữ",
    "đàn bà",
    "nữ",
    "con gái nuôi",
    "cô giáo",
]


MALE_WORDS: List[str] = [
    "trai",
    "con trai",
    "cậu bé",
    "anh trai",
    "em trai",
    "bạn trai",
    "cháu trai",
    "nam hoàng đế",
    "nam phục vụ",
    "cha",
    "ba",
    "bố",
    "cha dượng",
    "ba dượng",
    "bố dượng",
    "anh",
    "hắn",
    "ông",
    "chú",
    "dượng",
    "cậu",
    "ông ấy",
    "chú ấy",
    "chàng",
    "đàn ông",
    "nam",
    "con trai nuôi",
    "thầy",
]


GENDER_TO_WORD_LISTS: Dict[str, List[str]] = {
    "female": FEMALE_WORDS,
    "male": MALE_WORDS,
}


VIETNAMESE_NAMES: List[str] = [
    "Anh",
    "An",
    "Bảo",
    "Bình",
    "Châu",
    "Chi",
    "Cường",
    "Dũng",
    "Duy",
    "Đạt",
    "Đức",
    "Giang",
    "Hà",
    "Hải",
    "Hân",
    "Hạnh",
    "Hiếu",
    "Hiền",
    "Hoa",
    "Hoài",
    "Hoàng",
    "Hồng",
    "Hùng",
    "Huy",
    "Huyền",
    "Khánh",
    "Khang",
    "Khoa",
    "Kiên",
    "Kim",
    "Lan",
    "Linh",
    "Loan",
    "Long",
    "Mai",
    "Minh",
    "My",
    "Nam",
    "Ngân",
    "Nga",
    "Ngọc",
    "Nguyên",
    "Nhã",
    "Nhàn",
    "Nhi",
    "Nhiên",
    "Như",
    "Phong",
    "Phú",
    "Phúc",
    "Phương",
    "Quang",
    "Quân",
    "Quang",
    "Quốc",
    "Quỳnh",
    "Sơn",
    "Tâm",
    "Tân",
    "Tài",
    "Tâm",
    "Thanh",
    "Thảo",
    "Thái",
    "Thành",
    "Thắng",
    "Thảo",
    "Thi",
    "Thiên",
    "Thiện",
    "Thịnh",
    "Thúy",
    "Thu",
    "Thuận",
    "Thư",
    "Tiến",
    "Trang",
    "Trâm",
    "Trí",
    "Trinh",
    "Trúc",
    "Trung",
    "Tú",
    "Tuấn",
    "Tuyết",
    "Uyên",
    "Vân",
    "Vinh",
    "Việt",
    "Vy",
    "Xuân",
    "Yến",
    "Yên",
    "Lộc",
    "Đan",
    "Tiên",
    "Đào",
    "Hường",
    "Bích",
    "Tường",
]

ASIAN_NAMES: List[str] = [
    "cho",
    "wong",
    "tang",
    "huang",
    "chu",
    "chung",
    "ng",
    "wu",
    "liu",
    "chen",
    "lin",
    "yang",
    "kim",
    "chang",
    "shah",
    "wang",
    "li",
    "khan",
    "singh",
    "hong",
]

HISPANIC_NAMES: List[str] = [
    "castillo",
    "gomez",
    "soto",
    "gonzalez",
    "sanchez",
    "rivera",
    "martinez",
    "torres",
    "rodriguez",
    "perez",
    "lopez",
    "medina",
    "diaz",
    "garcia",
    "castro",
    "cruz",
]

WHITE_NAMES: List[str] = [
    "harris",
    "nelson",
    "robinson",
    "thompson",
    "moore",
    "wright",
    "anderson",
    "clark",
    "jackson",
    "taylor",
    "scott",
    "davis",
    "allen",
    "adams",
    "lewis",
    "williams",
    "jones",
    "wilson",
    "martin",
    "johnson",
]


RACE_TO_NAME_LISTS: Dict[str, List[str]] = {
    "vietnamese": VIETNAMESE_NAMES,
    "asian": ASIAN_NAMES,
    "hispanic": HISPANIC_NAMES,
    "white": WHITE_NAMES,
}


ADJECTIVE_LIST: List[str] = [
    "không tham nhũng",
    "nhàn nhã",
    "không cẩn thận",
    "mỉa mai",
    "bốc lửa",
    "cứng",
    "nhanh nhẹn",
    "kiêu ngạo",
    "yêu nước",
    "đòi hỏi",
    "điên",
    "vô trách nhiệm",
    "áp đảo",
    "bình thường",
    "khó chịu",
    "nghi ngờ",
    "bất mãn",
    "lau dọn",
    "không dung nạp",
    "anh hùng",
    "đánh đá",
    "không cá nhân",
    "phi logic",
    "nghiệt ngã",
    "tỉ mỉ",
    "long trọng",
    "chắc chắn",
    "khổ hạnh",
    "siêng năng",
    "hiền lành",
    "có thành kiến",
    "bẩn",
    "hòa đồng",
    "quả quyết",
    "hiền nhân",
    "ngớ ngẩn",
    "hiểu biết",
    "cảnh báo",
    "bận tâm",
    "cố ý",
    "thiếu suy nghĩ",
    "lệch lạc",
    "có học thức",
    "nghiêm túc",
    "nhẹ nhàng",
    "thô sơ",
    "tiện lợi",
    "dễ cáu bẳn",
    "báng bổ",
    "không trung thành",
    "mải mê",
    "chỉ đạo",
    "lành mạnh",
    "nhầm lẫn",
    "không thể hiểu được",
    "độc hại",
    "không trung thực",
    "không biết ơn",
    "bảo thủ",
    "chân thành",
    "ân cần",
    "hào phóng",
    "đánh đấm",
    "không màu",
    "thận trọng",
    "sự hiểu biết",
    "bắt chước",
    "đứng cách xa",
    "tích cực",
    "tự cao",
    "đáng ghét",
    "tinh tế",
    "phản bội",
    "hoang mang",
    "không lành mạnh",
    "lố bịch",
    "xa cách",
    "duy tâm",
    "hài hước",
    "tốt bụng",
    "quyết tâm",
    "tôn trọng",
    "thù hận",
    "vững vàng",
    "nguyên chất",
    "mâu thuẫn",
    "màu mè",
    "cơ khí",
    "không gây hại",
    "ngoan cố",
    "trẻ con",
    "tinh ranh",
    "ngọt ngào",
    "có thể thích nghi",
    "kỷ luật",
    "say đắm",
    "thoải mái",
    "tôn thờ",
    "tổ hợp",
    "bận rộn",
    "mượt mà",
    "hèn nhát",
    "êm dịu",
    "thân thiện",
    "giống đực",
    "khô khan",
    "ngay thẳng",
    "cá nhân hóa",
    "hung ác",
    "thôi miên",
    "có khát vọng",
    "yếu đuối",
    "nghiêm khắc",
    "thô thiển",
    "triệt để",
    "bình tĩnh",
    "khốn khổ",
    "đáp ứng",
    "thái quá",
    "đố kỵ",
    "rắc rối",
    "quanh co",
    "thần kinh",
    "mộc mạc",
    "thư giãn",
    "lạc hướng",
    "lịch lãm",
    "giàu trí tưởng tượng",
    "thẳng thừng",
    "mạnh mẽ",
    "khả nghi",
    "nhút nhát",
    "vô nhân tính",
    "văn hoá",
    "sợ hãi",
    "đánh bóng",
    "định kiến",
    "thất thường",
    "không gây khó chịu",
    "mô phạm",
    "bệnh hoạn",
    "sự phụ thuộc",
    "quan sát",
    "huyền ảo",
    "khoẻ mạnh",
    "đáng sợ",
    "thâm thúy",
    "danh dự",
    "đơn độc",
    "thử nghiệm",
    "vô cùng",
    "kìm hãm",
    "có kiểu cách",
    "không mục tiêu",
    "thông thường",
    "xác định",
    "kịch tính",
    "khách quan",
    "rõ ràng",
    "đàn áp",
    "ẻo lả",
    "cực đoan",
    "châm biếm",
    "gọn gàng",
    "trơn tru",
    "chia sẻ",
    "ghê tởm",
    "bề ngoài",
    "quan tâm",
    "tiến bộ",
    "lừa dối",
    "không vâng lời",
    "quái dị",
    "hào hùng",
    "thông minh",
    "dành riêng",
    "thuộc về chính trị",
    "đột ngột",
    "ranh mãnh",
    "ngốc nghếch",
    "không kiềm chế",
    "vô tín",
    "hẹp hòi",
    "rối loạn",
    "mềm mại",
    "tuỳ tiện",
    "tinh quái",
    "tận tụy",
    "hư hỏng",
    "vui vẻ",
    "đặc biệt",
    "đáng lo ngại",
    "hùng hồn",
    "không thận trọng",
    "bận",
    "phong nha",
    "hiếu học",
    "kỳ quái",
    "phù phiếm",
    "được tổ chức",
    "không thay đổi",
    "hợp tác",
    "vĩ đại",
    "vững chắc",
    "bị huỷ hoại",
    "tôn giáo",
    "vừa phải",
    "kìm kẹp",
    "bất kỳ",
    "kiên nhẫn",
    "chăm sóc",
    "mất trật tự",
    "thực nghiệm",
    "cẩn thận",
    "cân bằng",
    "láu cá",
    "khắc khe",
    "lãng mạn",
    "bực bội",
    "dễ cáu",
    "mãnh liệt",
    "cẩu thả",
    "đặt câu hỏi",
    "hời hợt",
    "quyến rũ",
    "có hiệu quả",
    "vô cảm",
    "phiền",
    "táo bạo",
    "kiềm chế",
    "ngọt",
    "đồng cảm",
    "ấn tượng",
    "cảnh giác",
    "nhạt nhẽo",
    "tự hào",
    "xảo trá",
    "tội phạm",
    "cách cư xử",
    "tức giận",
    "ghen tị",
    "ngu si đần độn",
    "không an toàn",
    "đời thường",
    "khỏe mạnh",
    "được giáo dục",
    "tử tế",
    "thiếu kiên nhẫn",
    "ma thuật",
    "phổ biến",
    "không suy nghĩ",
    "dễ bảo",
    "tiết kiệm",
    "khiêm tốn",
    "ảo tưởng",
    "quan phòng",
    "bối rối",
    "cân đối",
    "lúng túng",
    "hay thay đổi",
    "sáng tạo",
    "sai",
    "phản ứng",
    "dễ chịu",
    "phê bình",
    "chủ quan",
    "nhân tạo",
    "chậm",
    "thịnh soạn",
    "thiết thực",
    "thuyết phục",
    "dễ vỡ",
    "hiệu quả",
    "mở cửa",
    "nghiêm trang",
    "có trật tự",
    "lịch sự",
    "nông",
    "nhầm",
    "từ bi",
    "nản lòng",
    "không đều",
    "tinh khiết",
    "dục vọng",
    "thật ngạc nhiên",
    "chất rắn",
    "tràn đầy năng lượng",
    "thù địch",
    "yên tĩnh",
    "giáo điều",
    "ảm đạm",
    "trong suốt",
    "hoạt động",
    "thiếu trách nhiệm",
    "không hài lòng",
    "đáng ngưỡng mộ",
    "mê tín",
    "thiếu thận trọng",
    "tham",
    "mù quáng",
    "tính toán",
    "thích nghi",
    "dí dỏm",
    "ngạc nhiên",
    "đáng ngạc nhiên",
    "hoài nghi",
    "liêm khiết",
    "nghịch đảo",
    "tự phát",
    "nuông chiều",
    "cá nhân",
    "trung thực",
    "ngăn nắp",
    "chiến thắng",
    "bướng bỉnh",
    "ấm",
    "trách nhiệm",
    "cuồng loạn",
    "mơ màng",
    "trữ tình",
    "trực giác",
    "quên lãng",
    "rực rỡ",
    "ngu ngốc",
    "không khoan dung",
    "đáng yêu",
    "căng thẳng",
    "thống trị",
    "suy tư",
    "chủ nghĩa cá nhân",
    "không khỏe mạnh",
    "mịn",
    "kín đáo",
    "độc",
    "chiếm hữu",
    "sạch sẽ",
    "tráng lệ",
    "mơ mộng",
    "trưởng thành",
    "điềm tĩnh",
    "hiếu thảo",
    "giả dối",
    "mẹ",
    "vô hại",
    "dễ tiếp cận",
    "săn mồi",
    "chăm chỉ học hỏi",
    "chật hẹp",
    "đãng trí",
    "đáng thương",
    "gây rối",
    "hoà giải",
    "phiền hà",
    "nóng nảy",
    "bẩn thỉu",
    "lo lắng",
    "xảo quyệt",
    "hoà bình",
    "tham lam",
    "ham học",
    "nghiêm trọng",
    "nữ tính",
    "vui nhộn",
    "chính hãng",
    "ngu dốt",
    "có lịch sự",
    "cứng đầu",
    "tự tin",
    "ban đầu",
    "nhân từ",
    "dè dặt",
    "xâm lược",
    "lãnh đạm",
    "lạnh lẽo",
    "quan trọng",
    "cuồng tín",
    "có phương pháp",
    "khó",
    "cấp tiến",
    "phá hoại",
    "tin tưởng",
    "thân mật",
    "thoáng đãng",
    "thoáng",
    "gợi cảm",
    "vội vàng",
    "phê phán",
    "quyết đoán",
    "có lương tâm",
    "xấu xa",
    "thành kiến",
    "mê tín dị đoan",
    "lừa đảo",
    "điều khiển",
    "tinh vi",
    "đúng giờ",
    "phóng túng",
    "thanh lịch",
    "mạo hiểm",
    "trẻ trung",
    "cứng rắn",
    "thú vị",
    "cạnh tranh",
    "chính trị",
    "bảo vệ",
    "đê tiện",
    "tình cảm",
    "dũng cảm",
    "khó khăn",
    "sáng suốt",
    "khổ sở",
    "thanh bình",
    "làm nản lòng",
    "khô",
    "tùy tiện",
    "tham vọng",
    "ngông cuồng",
    "nhân ái",
    "hạn chế",
    "đáng ngờ",
    "giản dị",
    "nghỉ hưu",
    "vô tổ chức",
    "thô",
    "ổn định",
    "vâng lời",
    "đơn giản",
    "bảo mật",
    "phẫn nộ",
    "không biết",
    "khó hiểu",
    "rắn",
    "mộng mơ",
    "hùng biện",
    "thách thức",
    "thể thao",
    "dễ ảnh hưởng",
    "tự nhiên",
    "liên tục",
    "bị áp bức",
    "trơ trơ",
    "nguy hiểm",
    "đáng kính",
    "làm bối rối",
    "yên bình",
    "cố định",
    "bị kìm hãm",
    "chịu trách nhiệm",
    "có văn hóa",
    "khôn ngoan",
    "phản ánh",
    "hấp dẫn",
    "hoang phí",
    "tò mò",
    "khô cạn",
    "hữu ích",
    "rắn chắc",
    "vô hình",
    "phạm tội",
    "nóng tính",
    "lạnh",
    "có thể truy cập",
    "cầu kì",
    "khó ưa",
    "trẻ trâu",
    "mơ hồ",
    "tự do",
    "u ám",
    "trang nghiêm",
    "có trách nhiệm",
    "lòng trắc ẩn",
    "trung thành",
    "đồng ý",
    "tế nhị",
    "dốt",
    "náo nhiệt",
    "dịu dàng",
    "công bằng",
    "tha thứ",
    "phản chiếu",
    "không ổn định",
    "ấm áp",
    "không có niềm tin",
    "nhiệt tình",
    "vui tươi",
    "có hệ thống",
    "phụ thuộc",
    "xấu hổ",
    "ngốc ngếch",
    "sâu sắc",
    "thành thật",
    "hậu đậu",
    "đần độn",
    "trung lập",
    "tháo vát",
    "phức tạp",
    "phi thường",
    "không hợp lý",
    "cạn lời",
    "thô tục",
    "định mệnh",
    "bí mật",
    "trí tuệ",
    "dễ bị tổn thương",
    "lạc quan",
    "thanh tú",
    "nông cạn",
    "nghiêm ngặt",
    "khinh miệt",
    "duyên dáng",
    "có tổ chức",
    "nhẫn tâm",
    "phung phí",
    "dễ mến",
    "cô đơn",
    "thương xót",
    "hiện đại",
    "khắc kỷ",
    "xúc phạm",
    "hợp lý",
    "kiến thức",
    "riêng tư",
    "sở hữu",
    "trầm ngâm",
    "có kỷ luật",
    "vô mục đích",
    "kỳ cục",
    "yếu",
    "thong thả",
    "nghe lời",
    "cáu kỉnh",
    "xúc động",
    "im lặng",
    "độc lập",
    "hòa nhã",
    "vô vị",
    "biểu đạt",
    "man rợ",
    "hoà tan",
    "kiên định",
    "đứng đắn",
    "linh hoạt",
    "không thể hư hỏng",
    "nhỏ mọn",
    "khoan dung",
    "cứng nhắc",
    "có khả năng",
    "hợp tác xã",
    "tưởng tượng",
    "nhạy cảm",
    "yêu cầu",
    "chấp thuận",
    "biết ơn",
    "khờ dại",
    "bốc đồng",
    "thành công",
    "sai lầm",
    "người cha",
    "trung đoàn",
    "dễ thương",
    "phiền phức",
    "tuyệt vọng",
    "ít vận động",
    "hẹp hòi",
    "thẳng thắn",
    "khéo léo",
    "huyền bí",
    "hòa giải",
    "hung dữ",
    "lộn xộn",
    "đạm bạc",
    "lý tưởng hóa",
    "đáng tin cậy",
    "tàn nhẫn",
    "tầm thường",
    "xuất sắc",
    "ích kỷ",
    "bất cẩn",
    "lười",
    "vô ơn",
    "cùn",
    "học thuật",
    "oan trái",
    "không chịu trách nhiệm",
    "tốt lành",
    "phô trương",
    "gian dối",
    "nguyên bản",
    "sắc sảo",
    "can đảm",
    "tự kiêng",
    "tự mãn",
    "khinh thường",
    "thông cảm",
    "kiêu căng",
    "kỹ lưỡng",
    "vụng về",
    "đánh giá cao",
    "vô trung thành",
    "mạnh",
    "buồn rầu",
    "tàn bạo",
    "dã man",
    "hoà đồng",
    "trí não",
    "không tổ chức",
    "tỉnh táo",
    "sắc nét",
    "không đáng tin cậy",
    "đạo diễn",
    "dũng mãnh",
    "cảm xúc",
    "năng động",
    "bị ức chế",
    "nam tính",
    "xa hoa",
    "lạnh lùng",
    "ủ rũ",
    "đáng kính trọng",
    "không thực tế",
    "thụ động",
    "suy ngẫm",
    "chính thức",
    "trơ",
    "không thân thiện",
    "tập trung",
    "phản động",
    "hung hăng",
    "nồng nhiệt",
    "an toàn",
    "hủy hoại",
    "khinh bỉ",
    "chính xác",
    "tự phụ",
    "phi lý",
    "báo động",
    "dễ tổn thương",
    "kỳ lạ",
    "ồn ào",
    "gấp rút",
    "lý tưởng",
    "lạc lối",
    "minh bạch",
    "ý chí mạnh",
    "thoáng mát",
    "chu đáo",
    "gian lận",
    "quyết định",
    "thù hằn",
    "vui",
    "phục tùng",
    "ngây thơ",
    "phiêu lưu",
    "hay quên",
    "điên rồ",
    "nghệ thuật",
    "thẳng đứng",
    "tận tâm",
    "đáng khinh",
    "lười biếng",
    "thực tế",
    "đam mê",
    "ngạo mạn",
    "sâu",
]


PROFESSION_LIST: List[str] = [
    "người phục vụ",
    "nghệ sĩ piano",
    "người thể thao",
    "đặc phái viên",
    "người phát minh",
    "phóng viên ảnh",
    "người bảo vệ rừng",
    "nhà địa chất",
    "thanh thiếu niên",
    "nhân viên pha chế",
    "cầu thủ bóng đá",
    "ngư dân",
    "nhà tạo mẫu",
    "tổng thống",
    "thợ máy",
    "bình luận viên",
    "nhân viên cứu hộ",
    "trung uý",
    "bác sĩ nhi khoa",
    "nhà vật lý học",
    "trung sĩ",
    "nhà tâm lý học",
    "tay trống",
    "bộ trưởng mục sư",
    "tỏ tình",
    "nhà hoá học",
    "nhà kinh tế",
    "bác sĩ tâm thần",
    "thị trưởng",
    "diễn viên nam",
    "giáo sư",
    "họa sĩ tranh hoạt hình",
    "trung gian",
    "kế toán viên",
    "nhà nghiên cứu bệnh học",
    "ủy viên",
    "giọng ca",
    "người pha chế",
    "nhà thơ",
    "nghệ sĩ cello",
    "nhà thần kinh học",
    "người quản gia",
    "lính",
    "nhà dịch tễ học",
    "huấn luyện viên",
    "nhà khảo cổ học",
    "ca sĩ nhạc trữ tình",
    "nhà vận động",
    "người chơi trống",
    "học sinh",
    "bác sĩ da liễu",
    "nhà phân tích",
    "nghệ sĩ violin",
    "người thổi kèn trumpet",
    "thượng nghị sĩ",
    "người phát biểu cuối khóa",
    "tính cách",
    "người lao động",
    "vú em",
    "chính trị gia",
    "nhà soạn nhạc",
    "giám thị",
    "lao động",
    "công nhân",
    "quan chức",
    "bác sĩ tâm lý",
    "người sưu tập",
    "quản gia",
    "nghệ sĩ giải trí",
    "người bảo vệ",
    "giám tuyển",
    "nhà công nghiệp",
    "tiền vệ",
    "giảng viên",
    "nhà phát minh",
    "y tá",
    "người thổi kèn",
    "người bán hàng rong",
    "nhà nhân chủng học",
    "họa sĩ minh họa",
    "người môi giới",
    "người thám đo địa hình",
    "nhà xã hội học",
    "thay thế",
    "người ủng hộ",
    "người trông nom",
    "người làm vệ sinh",
    "thợ sửa chữa",
    "bảo trợ",
    "thủ môn",
    "giáo sĩ",
    "nam tước",
    "nhà soạn kịch",
    "nhà quay phim",
    "giám mục",
    "người thay thế",
    "quan sát viên",
    "người siêng năng",
    "người quay phim",
    "người giam giữ",
    "gia sư",
    "phục vụ nam",
    "nghệ sĩ guitar",
    "bác sĩ thần kinh",
    "nhà văn",
    "tiếp tân",
    "người bán thịt",
    "người biểu diễn",
    "sĩ quan",
    "cố vấn",
    "thợ làm đồ trang sức",
    "nữ diễn viên ballet",
    "truyện tranh",
    "giải phẫu thần kinh",
    "thầy tu",
    "chiến binh",
    "nhà chính trị",
    "uỷ viên hội đồng",
    "xạ thủ",
    "nhà nhân học",
    "quân nhân",
    "nhạc sĩ",
    "dưới thư ký",
    "chuyên gia",
    "nhà dược học",
    "học trò",
    "quay phim",
    "linh mục",
    "lập trình viên",
    "người viết chuyên mục",
    "người chơi violon",
    "quản đốc",
    "thợ điện",
    "nhân vật chính",
    "tuyên úy",
    "bác sĩ tim mạch",
    "nhà nghiên cứu",
    "người chăm sóc",
    "nhà khoa học",
    "nghị sĩ quốc hội",
    "người phụ trách",
    "nhà điều tra",
    "nhà lập pháp",
    "phụ tá",
    "gái điếm",
    "nhân vật",
    "tay chân đen",
    "người phản đối",
    "bác sĩ x quang",
    "hướng dẫn viên",
    "nhà vận động viên",
    "doanh nhân nữ",
    "người nội trợ",
    "bố",
    "thám tử",
    "đại sứ",
    "nhà thơ trữ tình",
    "người kể chuyện",
    "người chơi dương cầm",
    "người tuần tra",
    "lính cứu hoả",
    "thủ quỹ",
    "người sưu tầm",
    "chủ cửa hàng",
    "giáo viên",
    "nhân viên kế toán",
    "cầu thủ giữa sân",
    "thiện xạ",
    "kiểm soát viên",
    "bá tước",
    "học việc",
    "hiệu trưởng",
    "thợ làm bánh",
    "y tế",
    "người hòa giải",
    "người lính",
    "nhà bảo vệ môi trường",
    "nhà môi trường học",
    "nhà quảng bá",
    "người hầu",
    "người giám hộ",
    "biên tập viên",
    "người thăm dò ý kiến",
    "nhà sinh vật học",
    "thủ khoa",
    "người biểu diễn độc tấu",
    "học giả",
    "nữ vũ công ba lê",
    "nhà soạn lời bài hát",
    "chiến lược gia",
    "người lập pháp",
    "triết gia",
    "phái viên",
    "chủ nhà hàng",
    "nhà kinh tế học",
    "lễ tân",
    "vũ công",
    "cảnh sát trưởng",
    "truyền giáo viên",
    "phát thanh viên",
    "nhà viết kịch",
    "bí thư",
    "công dân",
    "chánh tòa",
    "người chơi saxophone",
    "kế hoạch",
    "người hoạt động chiến dịch",
    "người quen",
    "vận động viên",
    "người phục vụ nữ",
    "nhà bình luận",
    "thợ sửa ống nước",
    "họa sĩ",
    "nhà tổ chức",
    "doanh nhân tự do",
    "xã hội đen",
    "sinh viên",
    "nhà thám hiểm",
    "người chơi bóng",
    "tài xế taxi",
    "nhà toán học",
    "nhà văn thể thao",
    "nhà làm phim",
    "người bán hàng",
    "nữ diễn viên ba lê",
    "người cai",
    "mục sư",
    "giáo dân",
    "thợ mộc",
    "võ sĩ đấu vật",
    "thợ cắt tóc",
    "doanh nhân",
    "người chiến binh thánh chiến",
    "tuần tra viên",
    "nhà báo thể thao",
    "người thăm dò dư luận",
    "điều tra viên",
    "nhà hóa học",
    "chủ tịch",
    "tù nhân",
    "người thợ mổ",
    "đại tá",
    "tư vấn",
    "thượng thị",
    "tiếp viên",
    "lính cứu hỏa",
    "thầy tu do thái",
    "nữ diễn viên",
    "nghị sĩ",
    "người biện hộ",
    "thợ hớt tóc",
    "lính thủy",
    "ca sĩ",
    "công tố viên",
    "đầu bếp",
    "thư viện viên",
    "nữ phục vụ",
    "nhà điêu khắc",
    "thị trưởng hội đồng",
    "bác sĩ chẩn đoán hình ảnh",
    "nhà biên đạo múa",
    "cảnh sát tuần tra",
    "người hài kịch",
    "nhân viên văn phòng",
    "thủy thủ",
    "nhà từ thiện",
    "quản lý",
    "bác sĩ phẫu thuật",
    "nghệ sĩ biểu diễn",
    "nhân viên bán hàng",
    "nhà biên kịch",
    "đài truyền hình",
    "nhà ảo thuật",
    "biên kịch",
    "hoà giải viên",
    "nhân viên khảo sát",
    "người nổi tiếng",
    "người viết lời",
    "thẩm phán",
    "người hướng dẫn",
    "nghệ sĩ độc tấu",
    "người làm bánh",
    "tổng giám mục",
    "ông chủ",
    "nhân viên ngân hàng",
    "cai ngục",
    "diễn viên hài",
    "giám đốc trường học",
    "nhạc trưởng",
    "kiểm lâm",
    "người dẫn chuyện",
    "nhà môi giới chứng khoán",
    "cố vấn pháp luật",
    "nhà đàm phán",
    "người chơi đàn piano",
    "tên cướp",
    "tư tế",
    "thợ kim hoàn",
    "phán xét",
    "vận động viên thể thao",
    "nhà hảo tâm",
    "nhà tài trợ",
    "bồi bàn",
    "chủ sở hữu",
    "người chơi đàn guitar",
    "người quản lý",
    "nhà truyền giáo",
    "trung úy",
    "biên đạo múa",
    "trưởng khoa",
    "xã hội",
    "nhà ngoại giao",
    "phục vụ bàn",
    "hoạ sĩ",
    "gái mại dâm",
    "người làm vườn",
    "quản trị viên",
    "bộ trưởng",
    "người biểu tình",
    "thủ tướng",
    "nhà trị liệu",
    "nhà sử học",
    "thợ cơ khí",
    "chính khách",
    "nhà phê bình",
    "kế toán",
    "giám đốc",
    "tu sĩ",
    "hiệu trưởng đại học",
    "đội trưởng",
    "phó",
    "bán thịt",
    "linh mục tế",
    "chủ nhà trọ",
    "bác sĩ bệnh lý",
    "uỷ viên",
    "nhà thiên văn học",
    "nữ tu",
    "bác sĩ phẫu thuật thần kinh",
    "tư vấn viên",
    "thư ký",
    "bác sĩ",
    "giám hộ",
    "nhà giáo dục",
    "sát thủ",
    "trợ lý pháp lý",
    "tỷ phú",
    "chỉ huy",
    "nghệ sĩ",
    "nhân viên y tế",
    "người dự bị",
    "ông trùm",
    "diễn viên nữ",
    "người quản lý tài chính",
    "người hát rong",
    "nhiếp ảnh gia",
    "luật sư",
    "nhà công chúng học",
    "người bắn tỉa",
    "nữ doanh nhân",
    "nhà sư",
    "nông dân",
    "người lập kế hoạch",
    "giữ nhà",
    "kỹ thuật viên",
    "phóng viên",
    "thánh",
    "binh sĩ",
    "đô vật",
    "biện hộ",
    "người đàm phán",
    "đạo diễn",
    "tài xế xe tải",
    "thanh tra",
    "hài hước",
    "nhà báo",
    "nhà sưu tập",
    "người đại diện công tố",
    "họa sĩ truyện tranh",
    "tiểu thuyết gia",
    "trợ lý",
    "kiến trúc sư",
    "nhà thuyết giáo",
    "nhà vật lý",
    "tác giả",
    "bà nội trợ",
    "nhân viên kiểm lâm",
    "kẻ ám sát",
    "người làm việc nhà",
    "người chơi đàn organ",
    "hoạ sĩ minh hoạ",
    "quan viên",
    "thuyền trưởng",
    "ni cô",
    "thuỷ thủ",
    "nha sĩ",
    "người quan sát",
    "cầu thủ",
    "nguyên soái",
    "biểu diễn",
    "thiếu niên",
    "vệ sĩ",
    "dược sĩ",
    "diễn viên",
    "nhà tài chính",
    "thợ làm tóc",
    "thương nhân",
    "thủ thư",
    "bác sĩ phẫu thuật não",
    "người trông trẻ",
    "nhà tự nhiên học",
    "bảo mẫu",
    "cảnh sát",
    "nhân viên lễ tân",
    "ảo thuật gia",
    "y sĩ",
    "nghệ sĩ saxophone",
    "người môi giới bất động sản",
    "phi hành gia",
    "môi giới chứng khoán",
    "nhà địa chất học",
    "cha",
    "nhân viên",
    "người viết bài",
    "lao công",
    "người dọn dẹp",
    "người thông thạo",
    "võ sĩ quyền anh",
    "hội viên hội đồng",
    "chủ nhà",
    "người nổi loạn",
    "người gác cổng",
    "trợ lý luật sư",
    "ủy viên hội đồng",
    "phó thư ký",
    "môi giới",
    "thợ hàn",
]
