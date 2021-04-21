# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 13:50
# @Author  : lx
# @IDE ：PyCharm


# 其它 每个城市都有其它
cityItem = {
    "北京": ['东城区', '西城区', '朝阳区', '海淀区', '丰台区', '石景山区', '门头沟区', '通州区', '房山区', '昌平区', '大兴区', '顺义区', '怀柔区', '平谷区', '延庆县','密云县', '宣武区', '崇文区'],
    "上海": ['松江区','宝山区','金山区','嘉定区','南汇区','青浦区','浦东新区','奉贤区','徐汇区','静安区','闵行区','黄浦区','杨浦区','虹口区','普陀区','闸北区','长宁区','崇明县','卢湾区'],
    "重庆": ['万州区','涪陵区','渝中区','大渡口区','江北区','沙坪坝区','九龙坡区','南岸区','北碚区','綦江区','大足区','渝北区','巴南区','黔江区','长寿区','江津区','合川区','永川区','南川区','璧山区','铜梁区','潼南区','荣昌区','开州区','梁平区','武隆区','城口县','丰都县','垫江县','忠县','云阳县','奉节县','巫山县','巫溪县','彭水苗族土家族自治县','酉阳土家族苗族自治县','秀山土家族苗族自治县','石柱土家族自治县'],
    "天津": ['和平区','河东区','河西区','南开区','河北区','红桥区','东丽区','西青区','津南区','北辰区','武清区','宝坻区','滨海新区','宁河区','静海区','蓟州区'],
    "香港": ['中西区','湾仔区','东区','南区','油尖旺区','深水埗区','九龙城区','黄大仙区','观塘区','荃湾区','屯门区','元朗区','北区','大埔区','西贡区','沙田区','葵青区','离岛区'],
    "澳门": ['花地玛堂区','圣安多尼堂区','大堂区','望德堂区','风顺堂区','嘉模堂区','圣方济各堂区','路氹城','澳门新城区'],
    "宁夏": ["中卫", "银川", "吴忠", "石嘴山", "固原"],
    "河北": ["沧州", "石家庄", "唐山", "保定", "廊坊", "衡水", "邯郸", "邢台", "张家口", "辛集", "秦皇岛", "定州", "承德", "涿州"],
    "山西": ["太原", "阳泉", "晋城", "长治", "临汾", "运城", "忻州", "吕梁", "晋中", "大同", "朔州"],
    "山东": ["济南", "淄博", "聊城", "德州", "滨州", "济宁", "菏泽", "枣庄", "烟台", "威海", "泰安", "青岛", "临沂", "莱芜", "东营", "潍坊", "日照"],
    "河南": ["郑州", "新乡", "鹤壁", "安阳", "焦作", "濮阳", "开封", "驻马店", "商丘", "三门峡", "南阳", "洛阳", "周口", "许昌", "信阳", "漯河", "平顶山", "济源"],
    "广东": ["珠海", "中山", "肇庆", "深圳", "清远", "揭阳", "江门", "惠州", "河源", "广州", "佛山", "东莞", "潮州", "汕尾", "梅州", "阳江", "云浮", "韶关", "湛江", "汕头", "茂名"],
    "浙江": ["舟山", "温州", "台州", "绍兴", "衢州", "宁波", "丽水", "金华", "嘉兴", "湖州", "杭州"],
    "江苏": ["镇江", "扬州", "盐城", "徐州", "宿迁", "无锡", "苏州", "南通", "南京", "连云港", "淮安", "常州", "泰州"],
    "湖南": ["长沙", "邵阳", "怀化", "株洲", "张家界", "永州", "益阳", "湘西", "娄底", "衡阳", "郴州", "岳阳", "常德", "湘潭"],
    "吉林": ["长春", "长春", "通化", "松原", "四平", "辽源", "吉林", "延边", "白山", "白城"],
    "福建": ["漳州", "厦门", "福州", "三明", "莆田", "宁德", "南平", "龙岩", "泉州"],
    "甘肃": ["张掖", "陇南", "兰州", "嘉峪关", "白银", "武威", "天水", "庆阳", "平凉", "临夏", "酒泉", "金昌", "甘南", "定西"],
    "陕西": ["榆林", "西安", "延安", "咸阳", "渭南", "铜川", "商洛", "汉中", "宝鸡", "安康"],
    "辽宁": ["营口", "铁岭", "沈阳", "盘锦", "辽阳", "锦州", "葫芦岛", "阜新", "抚顺", "丹东", "大连", "朝阳", "本溪", "鞍山"],
    "江西": ["鹰潭", "宜春", "上饶", "萍乡", "南昌", "景德镇", "吉安", "抚州", "新余", "九江", "赣州"],
    "黑龙江": ["哈尔滨","鸡西", "黑河", "鹤岗", "大兴安岭", "绥化", "双鸭山", "齐齐哈尔", "伊春", "七台河", "牡丹江",  "佳木斯", "大庆"],
    "安徽": ["宣城", "铜陵", "六安", "黄山", "淮南", "合肥", "阜阳", "亳州", "安庆", "池州", "宿州", "芜湖", "马鞍山", "淮北", "滁州", "蚌埠"],
    "湖北": ["孝感", "武汉", "十堰", "荆门", "黄冈", "襄阳", "咸宁", "随州", "黄石", "恩施", "鄂州", "荆州", "宜昌", "潜江", "天门", "神农架", "仙桃"],
    "青海": ["西宁", "海西", "海东", "玉树", "黄南", "海南", "海北", "果洛"],
    "新疆": ["乌鲁木齐", "克州", "阿勒泰", "五家渠", "石河子", "伊犁", "吐鲁番", "塔城", "克拉玛依", "喀什", "和田", "哈密", "昌吉", "博尔塔拉", "阿克苏", "巴音郭楞", "阿拉尔", "图木舒克", "铁门关"],
    "贵州": ["铜仁", "黔东南", "贵阳", "安顺", "遵义", "黔西南", "黔南", "六盘水", "毕节"],
    "四川": ["遂宁", "攀枝花", "眉山", "凉山", "成都", "巴中", "广安", "自贡", "甘孜", "资阳", "宜宾", "雅安", "内江", "南充", "绵阳", "泸州", "凉山", "乐山", "广元", "甘孜", "德阳", "达州", "阿坝"],
    "广西": ["南宁", "贵港", "玉林", "梧州", "钦州", "柳州", "来宾", "贺州", "河池", "桂林", "防城港", "崇左", "北海", "百色"],
    "西藏": ["拉萨", "山南", "日喀则", "那曲", "林芝", "昌都", "阿里"],
    "云南": ["昆明", "红河", "大理", "玉溪", "昭通", "西双版纳", "文山", "曲靖", "普洱", "怒江", "临沧", "丽江", "红河", "迪庆", "德宏", "大理", "楚雄", "保山"],
    "内蒙古": ["呼和浩特", "乌兰察布", "兴安", "赤峰", "呼伦贝尔", "锡林郭勒", "乌海", "通辽", "巴彦淖尔", "阿拉善", "鄂尔多斯", "包头"],
    "海南": ["海口", "三沙", "三亚", "临高", "五指山", "陵水", "文昌", "万宁", "白沙", "乐东", "澄迈", "屯昌", "定安", "东方", "保亭", "琼中", "琼海", "儋州", "昌江"],
}

access_token = '此处填写'

headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Mobile Safari/537.36"}


JRlables =[
  {'lable1': '银行业', 'code': '0201'},{'lable1': '保险业', 'code': '0203'},{'lable1': '证券公司', 'code': '0202'},{'lable1': '小额贷款', 'code': '0213'},{'lable1': '互联网金融', 'code': '0215'},{'lable1': '消费金融', 'code': '0214'},{'lable1': '会计师事务所', 'code': '0210'},{'lable1': '资产管理公司', 'code': '0220'},{'lable1': '金融信息咨询/服务', 'code': '0218'},{'lable1': '第三方金融服务', 'code': '0219'},{'lable1': '风投/创业投资', 'code': '0208'},{'lable1': '期货公司', 'code': '0205'},{'lable1': '基金公司', 'code': '0204'},{'lable1': '信托公司', 'code': '0206'},{'lable1': '担保公司', 'code': '0207'},{'lable1': '金融租赁/融资租赁', 'code': '0212'},{'lable1': '投行', 'code': '0209'},{'lable1': '金融监管机构', 'code': '0221'},{'lable1': '拍卖/典当', 'code': '0211'},
  {'lable1': '工具软件', 'code': '0103'}, {'lable1': '企业级软件', 'code': '0108'}, {'lable1': 'IT系统集成/软件实施', 'code': '0126'}, {'lable1': '云计算/大数据/人工智能', 'code': '0107'}, {'lable1': '电子商务', 'code': '0104'}, {'lable1': '新零售', 'code': '0135'}, {'lable1': '互联网金融', 'code': '0215'}, {'lable1': '游戏开发/运营', 'code': '0105'}, {'lable1': '智能硬件', 'code': '0117'}, {'lable1': '社交网络', 'code': '0101'}, {'lable1': '社区/论坛', 'code': '0132'}, {'lable1': '新闻资讯/网媒/新媒体', 'code': '0115'}, {'lable1': '网络/新媒体营销', 'code': '0128'}, {'lable1': '在线旅游/酒店', 'code': '0118'}, {'lable1': 'O2O', 'code': '0110'}, {'lable1': '互联网出行', 'code': '011003'}, {'lable1': '视频网站/短视频/直播', 'code': '0114'}, {'lable1': '手机研发/制造', 'code': '110301'}, {'lable1': '音乐网站/云音乐', 'code': '0133'}, {'lable1': '搜索引擎/分类导航', 'code': '0116'}, {'lable1': '在线教育', 'code': '1411'}, {'lable1': '房产门户/交易网站', 'code': '030114'}, {'lable1': '招聘网站/在线招聘', 'code': '0120'}, {'lable1': '知识付费/内容变现', 'code': '0111'}, {'lable1': '互联网医疗平台', 'code': '130502'}, {'lable1': '信息/网络安全', 'code': '0124'}, {'lable1': 'IT软件外包', 'code': '0127'}, {'lable1': '电信运营增值服务', 'code': '0125'}, {'lable1': '大型房地产集团', 'code': '030101'}, {'lable1': '房地产开发', 'code': '030102'}, {'lable1': '房地产中介/销售代理', 'code': '030110'}, {'lable1': '房地产营销策划公司', 'code': '030112'}, {'lable1': '物业管理公司', 'code': '030104'}, {'lable1': '大型建筑集团', 'code': '030211'}, {'lable1': '房屋工程建筑施工', 'code': '030201'}, {'lable1': '土木工程建筑施工', 'code': '030202'}, {'lable1': '园林绿化/园林建设', 'code': '0303'}, {'lable1': '装修装饰公司/个体', 'code': '030208'}, {'lable1': '建筑安装', 'code': '030207'}, {'lable1': '家居行业/全屋定制', 'code': '0307'}, {'lable1': '建材批发/零售', 'code': '0308'}, {'lable1': '建筑材料制造', 'code': '030206'}, {'lable1': '钢结构行业', 'code': '0304'}, {'lable1': '工程监理公司', 'code': '0305'}, {'lable1': '工程项目管理/咨询', 'code': '040402'}, {'lable1': '建筑招投标/工程造价', 'code': '030204'}, {'lable1': '建筑勘察设计', 'code': '030203'}, {'lable1': '建筑设备制造/租赁', 'code': '030205'}, {'lable1': '房地产咨询/评估', 'code': '030111'}, {'lable1': '商业地产开发/运营', 'code': '030106'}, {'lable1': '产业地产/产业园区', 'code': '030108'}, {'lable1': '互联网装修', 'code': '030209'}, {'lable1': '房产门户/交易网站', 'code': '030114'}, {'lable1': '咨询行业', 'code': '0404'}, {'lable1': '财务咨询/服务', 'code': '0403'}, {'lable1': '法律咨询/服务', 'code': '0402'}, {'lable1': '人力资源咨询/服务', 'code': '0410'}, {'lable1': '企业管理/战略咨询公司', 'code': '0401'}, {'lable1': '猎头行业', 'code': '0415'}, {'lable1': '外包/劳务派遣公司', 'code': '0427'}, {'lable1': '安保服务', 'code': '0420'}, {'lable1': '商务信息咨询/代理', 'code': '0426'}, {'lable1': '房地产中介/销售代理', 'code': '030110'}, {'lable1': '留学/移民中介', 'code': '1414'}, {'lable1': '市场调研服务', 'code': '0407'}, {'lable1': '营销策划服务公司', 'code': '0416'}, {'lable1': '企业培训服务', 'code': '0428'}, {'lable1': '知识产权服务', 'code': '0409'}, {'lable1': '检测认证服务', 'code': '0411'}, {'lable1': '评估服务', 'code': '0419'}, {'lable1': '会议展览服务', 'code': '0412'}, {'lable1': '办公设备/办公服务', 'code': '0417'}, {'lable1': '征信/信用服务公司', 'code': '0421'}, {'lable1': '旅游业', 'code': '0503'}, {'lable1': '广告业', 'code': '0602'}, {'lable1': '物流公司/货运', 'code': '1606'}, {'lable1': '租赁行业', 'code': '0424'}, {'lable1': '物业管理公司', 'code': '030104'}, {'lable1': '翻译服务', 'code': '0418'}, {'lable1': '餐饮业', 'code': '0501'}, {'lable1': '酒店/住宿业', 'code': '0502'}, {'lable1': '旅游业', 'code': '0503'}, {'lable1': '美发/美容/美甲服务', 'code': '0506'}, {'lable1': '娱乐/休闲/游乐服务', 'code': '0505'}, {'lable1': '按摩/保健/养生服务', 'code': '0512'}, {'lable1': '洗浴服务', 'code': '0511'}, {'lable1': '运动健身服务', 'code': '0507'}, {'lable1': '婚庆服务', 'code': '0508'}, {'lable1': '摄影服务', 'code': '0509'}, {'lable1': '快递/配送行业', 'code': '1607'}, {'lable1': '物流公司/货运', 'code': '1606'}, {'lable1': '出租车行业', 'code': '1610'}, {'lable1': '互联网用车', 'code': '1612'}, {'lable1': '驾校/陪练行业', 'code': '1418'}, {'lable1': '代驾服务', 'code': '0525'}, {'lable1': '汽车租赁', 'code': '1009'}, {'lable1': '物业管理公司', 'code': '030104'}, {'lable1': '保安/停车场服务', 'code': '0527'}, {'lable1': '家政保洁服务', 'code': '0504'}, {'lable1': '装修装饰公司/个体', 'code': '030208'}, {'lable1': '电梯/水电/物业维修', 'code': '0528'}, {'lable1': '家电维修', 'code': '0520'}, {'lable1': '汽车修理厂', 'code': '100402'}, {'lable1': '洗衣/剪裁/皮革护理', 'code': '0513'}, {'lable1': '服装服饰行业', 'code': '0802'}, {'lable1': '心理咨询行业', 'code': '1313'}, {'lable1': '图文快印/打印/复印服务', 'code': '0514'}, {'lable1': '搬家/搬运服务', 'code': '0516'}, {'lable1': '亲子/托儿服务', 'code': '0517'}, {'lable1': '宠物服务', 'code': '0518'}, {'lable1': '其他维修', 'code': '0522'}, {'lable1': '殡葬服务', 'code': '0523'}, {'lable1': '广告业', 'code': '0602'}, {'lable1': '公关公司', 'code': '0603'}, {'lable1': '广播电视媒体', 'code': '0601'}, {'lable1': '报纸/杂志媒体', 'code': '0612'},
  {'lable1': '新闻资讯/网媒/新媒体', 'code': '0115'}, {'lable1': '自媒体/自由撰稿人', 'code': '0613'}, {'lable1': '图书出版/发行', 'code': '0606'}, {'lable1': '影视制作/发行', 'code': '0607'}, {'lable1': '演出/演艺/经纪行业', 'code': '0609'}, {'lable1': '音乐产业', 'code': '0616'}, {'lable1': '公共文化场馆', 'code': '0615'}, {'lable1': '艺术品/美术品/画廊', 'code': '0614'}, {'lable1': '文创产品/文化IP', 'code': '0608'}, {'lable1': '体育产业', 'code': '0610'}, {'lable1': '文教办公用品', 'code': '0815'}, {'lable1': '娱乐/休闲/游乐服务', 'code': '0505'}, {'lable1': '会议展览服务', 'code': '0412'}, {'lable1': '婚庆服务', 'code': '0508'}, {'lable1': '摄影服务', 'code': '0509'}, {'lable1': '图文快印/打印/复印服务', 'code': '0514'}, {'lable1': '印刷包装行业', 'code': '0919'}, {'lable1': '个护清洁/化妆品行业', 'code': '0701'}, {'lable1': '食品生产/加工行业', 'code': '0702'}, {'lable1': '乳制品行业', 'code': '0707'}, {'lable1': '酒类行业', 'code': '0704'}, {'lable1': '饮品/饮料行业', 'code': '0703'}, {'lable1': '方便食品/速食品行业', 'code': '0709'}, {'lable1': '面包糕点烘焙', 'code': '0718'}, {'lable1': '生鲜食品行业', 'code': '0710'}, {'lable1': '粮油行业', 'code': '0712'}, {'lable1': '调味品行业', 'code': '0708'}, {'lable1': '营养保健品行业', 'code': '0711'}, {'lable1': '茶叶行业', 'code': '0705'}, {'lable1': '烟草业', 'code': '0706'}, {'lable1': '母婴用品', 'code': '0715'}, {'lable1': '制糖业', 'code': '0713'}, {'lable1': '计生用品', 'code': '0714'}, {'lable1': '超市行业', 'code': '120202'}, {'lable1': '食品饮料烟酒批发', 'code': '120101'}, {'lable1': '食品饮料烟酒零售', 'code': '120204'}, {'lable1': '宠物食品/用品', 'code': '0716'}, {'lable1': '造纸与纸制品业', 'code': '0918'}, {'lable1': '服装服饰行业', 'code': '0802'}, {'lable1': '制鞋业', 'code': '0803'}, {'lable1': '皮具箱包行业', 'code': '0804'}, {'lable1': '家用电器行业', 'code': '0801'}, {'lable1': '家具/家居行业', 'code': '0810'}, {'lable1': '智能家居', 'code': '0812'}, {'lable1': '家纺用品行业', 'code': '0811'}, {'lable1': '厨房炊具/卫浴洁具', 'code': '0813'}, {'lable1': '日用小商品', 'code': '0814'}, {'lable1': '奢侈品/首饰/珠宝行业', 'code': '0817'}, {'lable1': '百货商场/卖场/购物中心', 'code': '120201'}, {'lable1': '工艺品/礼品行业', 'code': '0823'}, {'lable1': '手机研发/制造', 'code': '110301'}, {'lable1': '电脑/电脑配件生产制造', 'code': '0808'}, {'lable1': '数码/影音产品', 'code': '0806'}, {'lable1': '智能硬件', 'code': '0117'}, {'lable1': '钟表行业', 'code': '0824'}, {'lable1': '眼镜行业', 'code': '0825'}, {'lable1': '玩具行业', 'code': '0818'}, {'lable1': '文教办公用品', 'code': '0815'}, {'lable1': '体育/运动服饰装备', 'code': '0820'}, {'lable1': '乐器制造', 'code': '0816'}, {'lable1': '纺织业', 'code': '0901'}, {'lable1': '橡胶和塑料制品业', 'code': '0904'}, {'lable1': '化工原料/材料/制品', 'code': '0905'}, {'lable1': '冶金行业', 'code': '0906'}, {'lable1': '金属/五金制品业', 'code': '0907'}, {'lable1': '通用机械设备制造', 'code': '0914'}, {'lable1': '专用机械设备制造', 'code': '0915'}, {'lable1': '机械修理/维修/金属修理', 'code': '0916'}, {'lable1': '木材加工/木、竹、草制品', 'code': '0920'}, {'lable1': '皮、革、羽毛制造', 'code': '0921'}, {'lable1': '建筑材料制造', 'code': '030206'}, {'lable1': '水泥制造/混凝土生产', 'code': '0927'}, {'lable1': '玻璃制造', 'code': '0909'}, {'lable1': '陶瓷制造', 'code': '0910'}, {'lable1': '电力电气设备制造', 'code': '150503'}, {'lable1': '仪器仪表制造', 'code': '0913'}, {'lable1': '工业自动化', 'code': '0928'}, {'lable1': '交通设备制造', 'code': '0917'}, {'lable1': '计算机/电子/通信设备制造', 'code': '0911'}, {'lable1': '造纸与纸制品业', 'code': '0918'}, {'lable1': '印刷包装行业', 'code': '0919'}, {'lable1': '石油化工行业', 'code': '0902'}, {'lable1': '医药制造业', 'code': '130201'}, {'lable1': '废弃资源利用', 'code': '0922'},
  {'lable1': '快速消费品', 'code': '07'}, {'lable1': '耐用消费品', 'code': '08'}, {'lable1': '汽车生产制造', 'code': '1001'}, {'lable1': '汽车零配件', 'code': '1002'}, {'lable1': '汽车销售/批发/外贸', 'code': '1003'}, {'lable1': '汽车售后/维修/养护', 'code': '1004'}, {'lable1': '汽车用品制造', 'code': '1011'}, {'lable1': '二手车交易', 'code': '1005'}, {'lable1': '汽车租赁', 'code': '1009'}, {'lable1': '互联网造车', 'code': '1013'}, {'lable1': '汽车金融', 'code': '0216'}, {'lable1': '汽车保险', 'code': '1008'}, {'lable1': '汽车IT/车联网/自动驾驶', 'code': '1006'}, {'lable1': '汽车文化产业/车友会', 'code': '1010'},{'lable1': '电信运营商', 'code': '1101'}, {'lable1': '通信/网络设备商', 'code': '1102'},
  {'lable1': '手机/通信终端制造', 'code': '1103'}, {'lable1': '通信系统集成商', 'code': '1105'}, {'lable1': '通信设计院', 'code': '1107'}, {'lable1': '通信软件研发', 'code': '1106'}, {'lable1': '通信工程设计/施工', 'code': '1109'}, {'lable1': '通信基础设施建设', 'code': '1108'}, {'lable1': '电子/半导体行业', 'code': '1104'}, {'lable1': '光电子行业', 'code': '1113'}, {'lable1': '消费电子行业', 'code': '110406'}, {'lable1': '精密元器件/模具', 'code': '1116'}, {'lable1': '广电网络/设备', 'code': '1117'}, {'lable1': '5G技术', 'code': '1110'}, {'lable1': '批发业', 'code': '1201'}, {'lable1': '零售业', 'code': '1202'}, {'lable1': '进出口贸易', 'code': '1203'}, {'lable1': '贸易代理公司', 'code': '1204'}, {'lable1': '电子商务', 'code': '0104'}, {'lable1': '淘宝店/微商', 'code': '1209'}, {'lable1': '个体批发零售', 'code': '1210'}, {'lable1': '印刷包装行业', 'code': '0919'}, {'lable1': '医院', 'code': '130101'}, {'lable1': '社区医疗/卫生院', 'code': '130102'}, {'lable1': '诊所/门诊部', 'code': '130103'}, {'lable1': '医药行业', 'code': '1302'}, {'lable1': '医疗器械', 'code': '1303'}, {'lable1': '医疗美容/整形', 'code': '1308'}, {'lable1': '健康体检', 'code': '1306'}, {'lable1': '妇幼保健院', 'code': '130104'}, {'lable1': '疾病预防控制中心', 'code': '130106'}, {'lable1': '第三方医学检验', 'code': '1312'}, {'lable1': '心理咨询行业', 'code': '1313'}, {'lable1': '医疗医药科研/基因工程', 'code': '1307'}, {'lable1': '医疗信息化/互联网医疗', 'code': '1305'}, {'lable1': '康复中心/疗养院', 'code': '1311'}, {'lable1': '幼儿园/早教机构', 'code': '140101'}, {'lable1': '小学', 'code': '140102'}, {'lable1': '初中', 'code': '140103'}, {'lable1': '高中', 'code': '140104'}, {'lable1': '大学/公办高校', 'code': '140201'}, {'lable1': '民办高校', 'code': '140202'}, {'lable1': '职业学校/中专/技校', 'code': '1403'}, {'lable1': '成人学历教育机构', 'code': '1405'}, {'lable1': 'k12教育培训/辅导', 'code': '1406'}, {'lable1': '在线教育', 'code': '1411'}, {'lable1': '技能/资格认证培训', 'code': '140803'}, {'lable1': '外语培训机构', 'code': '140807'}, {'lable1': '艺术/体育培训机构', 'code': '1420'}, {'lable1': '留学/移民中介', 'code': '1414'}, {'lable1': '国际学校', 'code': '1415'}, {'lable1': 'MBA/商学院/管理培训', 'code': '140806'}, {'lable1': '科研机构', 'code': '1409'}, {'lable1': '科研成果转化', 'code': '1410'}, {'lable1': '特殊教育学校/机构', 'code': '1416'}, {'lable1': '兴趣辅导机构', 'code': '1417'}, {'lable1': '教材/教辅资料', 'code': '1407'}, {'lable1': '驾校/陪练行业', 'code': '1418'}, {'lable1': '煤炭行业', 'code': '1501'}, {'lable1': '石油行业', 'code': '1502'}, {'lable1': '天然气/燃气行业', 'code': '1503'}, {'lable1': '电力/电气行业', 'code': '1505'}, {'lable1': '核电/核能产业', 'code': '1504'}, {'lable1': '新能源产业/新能源发电', 'code': '1507'}, {'lable1': '电池行业', 'code': '1506'}, {'lable1': '采矿业', 'code': '1508'}, {'lable1': '水利行业', 'code': '1509'}, {'lable1': '热力行业', 'code': '1510'}, {'lable1': '供水/水务行业', 'code': '1512'}, {'lable1': '环保治理/环境监测', 'code': '1514'}, {'lable1': '冶金行业', 'code': '0906'}, {'lable1': '铁路运输业', 'code': '1601'},
  {'lable1': '航空运输业', 'code': '1603'}, {'lable1': '水路航运业', 'code': '1604'},{'lable1': '管道运输业', 'code': '1605'}, {'lable1': '货运代理/报关', 'code': '1618'},
  {'lable1': '物流公司/货运', 'code': '1606'}, {'lable1': '供应链管理', 'code': '1623'}, {'lable1': '快递/配送行业', 'code': '1607'}, {'lable1': '公交/客运公司', 'code': '1611'}, {'lable1': '地铁/轻轨', 'code': '1609'}, {'lable1': '出租车行业', 'code': '1610'}, {'lable1': '互联网用车', 'code': '1612'}, {'lable1': '仓储服务/仓储管理', 'code': '1620'},
  {'lable1': '装卸搬运/吊装', 'code': '1617'}, {'lable1': '高速公路运营管理', 'code': '1608'},
  {'lable1': '交通设备制造', 'code': '0917'}, {'lable1': '交通设施', 'code': '1614'},
  {'lable1': '交通规划设计', 'code': '1615'}, {'lable1': '客票代理', 'code': '1619'}, {'lable1': '邮政业', 'code': '1621'}, {'lable1': '农业', 'code': '1701'}, {'lable1': '林业/苗木', 'code': '1702'}, {'lable1': '畜牧业', 'code': '1703'}, {'lable1': '渔业/水产', 'code': '1704'}, {'lable1': '园林绿化/园林建设', 'code': '0303'}, {'lable1': '饲料生产加工', 'code': '1708'}, {'lable1': '化肥制造', 'code': '090502'}, {'lable1': '农药制造', 'code': '090503'}, {'lable1': '粮油行业', 'code': '0712'}, {'lable1': '生鲜行业', 'code': '1706'}, {'lable1': '乳制品行业', 'code': '0707'}, {'lable1': '制糖业', 'code': '0713'}, {'lable1': '农业/农机合作社', 'code': '1713'}, {'lable1': '林业/苗木合作社', 'code': '1714'}, {'lable1': '养殖/畜牧合作社', 'code': '1715'}, {'lable1': '渔业/水产合作社', 'code': '1716'}, {'lable1': '木材加工/木、竹、草制品', 'code': '0920'}, {'lable1': '渔具钓具行业', 'code': '1717'}, {'lable1': '农业生产服务/技术服务', 'code': '1709'}, {'lable1': '畜禽技术服务', 'code': '1711'}, {'lable1': '水产/渔业技术服务', 'code': '1718'}, {'lable1': '农民工', 'code': '1719'}, {'lable1': '中国共产党机关', 'code': '1801'},
  {'lable1': '国务院/地方各级政府', 'code': '1802'},{'lable1': '各部委及下属厅、局', 'code': '1803'}, {'lable1': '公安机关/派出所', 'code': '1810'}, {'lable1': '法院/检察院', 'code': '1804'}, {'lable1': '居委会/村委会', 'code': '180706'}, {'lable1': '街道办事处', 'code': '1811'}, {'lable1': '人民政协/民主党派', 'code': '1805'}, {'lable1': '社会团体/组织', 'code': '1807'},
  {'lable1': '国际机构/组织', 'code': '1808'},{'lable1': '事业单位', 'code': '1806'}
]