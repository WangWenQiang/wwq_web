/**
 * Created by wangwenqiang on 2017/12/27.
 */

//ajax testing
function DoAjax() {
    var tmp = $("#www").val();
    var sample_id = $("#sampleID").val();
    $.ajax({
        url: "/fresh",
        async: false,
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        type: "POST",
        data: {operate: tmp, sample_id: sample_id},
        success: function (arg) {
            var obj = jQuery.parseJSON(arg);
            $("#eee").val(obj.operate);
        }
    })
}

//重置被选中的style
function reset_radio_style() {
    var all_a = document.getElementsByTagName("a");
    for (var a_tag = 0; a_tag < all_a.length; a_tag++) {
        all_a[a_tag].style.backgroundColor = "";
    }
}

//保存行为-ajax-from方法
function saveActions() {
    var options = {
        url: "/act",
        success: function (msg) {
            var act_no = msg["act_no"];
            var h_acts = msg["history_acts"];
            actNo = document.getElementById("actNo");
            actNo.value = act_no;

            history_acts = document.getElementById("history_actions");
            $("#history_actions li").remove();
            // history_acts.removeChild();
            for (var i = 0; i < h_acts.length; i++) {
                var elem_li = document.createElement("li");
                elem_li.innerHTML = h_acts[i];
                history_acts.appendChild(elem_li);
            }
            return false;
        },
        error: function (msg) {
            alert(msg["error"]);
            return false;
        },
        clearForm: true,
        restForm: true,
        timeout: 100000
    };
    $("#myForm_act").ajaxSubmit(options);
}

//保存打分-ajax-from方法
function saveScore() {
    var options = {
        url: "/score",
        success: function () {
            reset_radio_style();
            // show_commit();
        },
        error: function () {
            reset_radio_style();
            // show_commit();
        },
        clearForm: true,
        timeout: 100000
    };
    $("#myForm").ajaxSubmit(options);
}

//保存打分-一般方法
function submit_all() {
    document.myForm.action = "/score";
    document.myForm.submit();
}

//更新历史行为
function change_history_action() {
    var list_cell = document.getElementById("history_action").getElementsByTagName("li");
    var all_value = [];
    for (var i = 0; i < list_cell.length; i++) {
        all_value.push(list_cell[i].innerHTML);
    }
}

//被选中后的style变化
function radio_select(radio_id, name) {
    var line_radio = document.getElementsByName(name);
    var label_id = "a_" + radio_id;
    for (var k = 0; k < line_radio.length; k++) {
        var tmp_radio = line_radio[k];
        if (tmp_radio.id == label_id) {
            tmp_radio.style.backgroundColor = "#007bff";
        } else {
            tmp_radio.style.backgroundColor = "";
        }
    }
}

//建议方向联动具体行为
function acion_select(x) {
    //获取一级菜单长度
    var male_direction = ["精心的形象打扮", "注重服装搭配", "有爱的言语举止", "合理的情绪表达", "发现对方的兴趣爱好", "营造浪漫的氛围", "创造机会去接近对方",
        "多一些身体接触", "制造意想不到的惊喜", "互相了解生活状态", "提升彼此的交流质量", "保持良好的心理状态", "适当表达内心想法",
        "更多的行动来表达爱", "表现得更有责任心", "更坦诚的展示自我", "体现对感情的用心", "对情感态度的诚恳", "感谢对方的付出",
        "充满爱的言语交流", "深情地进行身体接触", "肯定对方的所作所为", "提升共处时的幸福感", "经常送一些爱的礼物", "试着为对方服务",
        "需要避免的行为举止", "需改善的心理状态", "避免言语上的攻击", "日常行为上的改善", "表现出彼此间的爱", "互相表露真实的内心"];
    var male_advice = [["理一个精神点的发型", "出门前认真打理一下胡子", "保持指甲的清洁度，不要留长", "注意牙齿洁白，口气清新"], ["颜色组合尽量不超过三种", "避免过于另类的搭配", "约会前换一套干净的衣服和鞋子"], ["眼神交流，聊天时可以多看着TA的眼睛", "睡前的甜蜜问候，哪怕只是一句“晚安”", "发自内心，真诚赞美对方的穿着打扮", "经常在社交网络上为TA点赞、留言", "把封闭式问题改成开放式问题，避免询问只能回答是否的问题", "TA说话时给予积极回应，可以试着多点点头，表达肯定对方观点的言辞", "走在马路上的时候，主动走在外侧，让TA走在内侧", "要相对谨慎地做出一些亲密举动"], ["经常展现灿烂的微笑，表达心中的喜悦", "聊天时避免抱怨，不要传递负能量", "交流时避免说脏话，保持基本素养", "避免夸夸其谈，避免八卦话题"], ["了解TA喜欢的电影、音乐和书籍", "观察TA平时喜欢吃的美食", "留意TA的一些生活习惯，发现TA的特殊细节", "在对方的社交网络上找共同的兴趣爱好，去点赞留言", "适当展示你的学识才华，表现一些你的特长"], ["独处时放一曲浪漫的音乐", "房间内来一点薰衣草的香薰", "约在一个安静的咖啡馆，闲聊下午时光"], ["偶尔送个不贵重的小礼物", "积极关注对方生活状态，找机会给予帮助", "给TA买一些爱吃的零食"], ["合适的时机，可以尝试握住TA的手", "一起过马路时，轻轻搂着TA的腰", "不经意间，缕缕TA的发丝"], ["提前为TA准备爱吃的早饭", "一起去游乐园，尝试不同的游玩项目", "在特殊的日子，送TA一份有心意的礼物"], ["合适的时机聊聊彼此的近期的工作、学习经历", "与TA分享你遇到过的有趣的事", "带上TA一起参加朋友聚会", "分享彼此的生活情绪", "可以试着共同养一只宠物"], ["适当玩笑，让交流的氛围更加轻松", "挑一个对方感兴趣的话题，试着去展开分享彼此观点", "夸奖TA的想法或观点，增强交流分享的动力", "给对方起一个合适的昵称", "做决定前，多询问TA的意见，考虑TA的感受"], ["避免去刨根问底，不要带给TA很大的压力", "提升自身的学识能力，增加吸引力"], ["适当表露自己内心的烦恼或心事"], ["主动给TA一个紧紧的拥抱，温柔的亲吻", "挑一个TA喜欢的目的地，来一场属于两个人的旅行", "对于TA的亲密举动给予积极的回应"], ["避免轻易做承诺，但答应过的事一定要完成", "不要一味的让对方付出，需要适当的给予回馈"], ["合适的时机让TA了解你的家庭背景", "避免刻意掩盖自身缺点，试着用自嘲的方式来表露", "不要总把一些不满的情绪刻意隐藏，可以有适当的发泄"], ["在你们的纪念日，准备惊喜，讲讲往日相处时的幸福瞬间", "向TA表露你对于彼此未来的美好愿景与规划", "培养彼此间的默契，可以是简单的动作，也可是思维上的一致"], ["不逃避所面临的问题，试着表露彼此真实想法", "不要太过敏感，避免胡思乱想，互相猜忌"], ["第一时间感谢TA为你做的任何事情", "找合适的机会犒劳TA的付出，买份礼物、请顿大餐"], ["向对方说一声“我爱你”", "合适的时机，告诉对方“亲爱的，我为你感到骄傲”", "交流时，对于TA的想法，不要轻易打断去做评价批评", "告诉TA“你对我而言非常重要，甚至胜于一切”", "发现TA累的时候，及时上前安慰，“亲爱的，我能为你做些什么，能让你感觉好一些？”"], ["相处时深情抱住TA，持续10秒钟以上", "不忘给TA一个早安吻、晚安吻或见面吻", "坐在一起时，可以互相靠着对方", "找个合适的机会，轻轻抚摸TA的背部"], ["对TA为你做的一件事表示赞赏、肯定或感激", "让对方知道自己最信任的人就是TA"], ["试着都不玩手机，花一段时间与TA独处", "来一场只属于两个人的长途旅行", "找个你们平时不常做的活动，一起完成一次"], ["为TA写一份爱的便笺或书信", "在TA不知情的时候，带一样TA最喜欢吃的东西", "准备一份TA想要很久但一直没有舍得买的东西作为礼物"], ["帮TA洗洗衣服，换换床单，打扫一下房间", "为TA精心准备一次丰盛的晚餐", "为了TA，做一件你平时不爱做但TA非常喜欢的事"], ["避免不合理的挑剔，觉得自己更胜一筹，而抓住TA的缺点不放", "避免草率的做出负面评价，不要轻易把问题原因直接归咎于TA", "不要逃避，避免在沟通时沉默、走开，不愿意就问题进行讨论", "避免表现过于傲慢，不要在TA犯错的时候小题大做，不愿宽恕", "不要做监视对方的行为，需要留一些私人空间"], ["试着放下内心强烈的自我防御，去认可对方，去做出一些自我调整与改变", "试着让步，退回到与TA平等的状态上，给予双方平等沟通的权利", "不要为自己免责，有错误也需要承认", "不要忽视对方的看法，只顾自身感受"], ["避免使用贬低的称呼，或者恶劣的态度语气与TA交流", "感谢TA努力对情感做出的表达，哪怕显得笨拙，也不要嘲笑"], ["试着保持同步的上床睡觉时间", "试着培养共同的兴趣爱好，周末一同去参加"], ["试着在公共场合或社交媒体上秀恩爱", "经常性地直接表达“我爱你”之类的甜言蜜语", "认真对待TA喜欢的事物，尝试理解他的需求", "肯定TA的负面情绪，在TA难过、愤怒、挫败时感受到你的支持和依靠"], ["试着共享彼此的社交，邀请彼此的朋友、亲人，并介绍互相认识", "试着去共同承担一些责任"]];

    var female_direction = ["精心的妆容打扮", "注重服装搭配", "有爱的言语举止", "合理的情绪表达", "发现对方的兴趣爱好", "营造浪漫的氛围", "创造机会去接近对方",
        "多一些身体接触", "制造意想不到的惊喜", "互相了解生活状态", "提升彼此的交流质量", "保持良好的心理状态", "适当表达内心想法",
        "更多的行动来表达爱", "表现得更有责任心", "更坦诚的展示自我", "体现对感情的用心", "对情感态度的诚恳", "感谢对方的付出",
        "充满爱的言语交流", "深情地进行身体接触", "肯定对方的所作所为", "提升共处时的幸福感", "经常送一些爱的礼物", "试着为对方服务",
        "需要避免的行为举止", "需改善的心理状态", "避免言语上的攻击", "日常行为上的改善", "表现出彼此间的爱", "互相表露真实的内心"];
    var female_advice = [["化一个简单精致的妆容，体现自己的风格", "做一个美美的发型", "注意牙齿洁白，口气清新"], ["穿着干净整洁，可以搭配稍许香水，让自己显得自信", "约会时尽量避免职业装，太过严肃的搭配", "颜色组合尽量不超过三种", "避免过于另类的搭配"], ["可以有稍微的示弱，让TA主动来保护你", "眼神交流，聊天时可以多看着TA的眼睛", "睡前的甜蜜问候，哪怕只是一句“晚安”", "经常在社交网络上为TA点赞、留言", "TA说话时给予积极回应，可以试着多点点头，表达肯定对方观点的言辞", "要相对谨慎地做出一些亲密举动"], ["经常展现灿烂的微笑，表达心中的喜悦", "聊天时避免抱怨，不要传递负能量", "交流时避免说脏话，保持基本素养", "避免夸夸其谈，避免八卦话题"], ["了解TA喜欢的电影、音乐和书籍", "观察TA平时喜欢吃的美食", "留意TA的一些生活习惯，发现TA的特殊细节", "在对方的社交网络上找共同的兴趣爱好，去点赞留言", "适当展示你的学识才华，表现一些你的特长"], ["独处时放一曲浪漫的音乐", "房间内来一点薰衣草的香薰", "约在一个安静的咖啡馆，闲聊下午时光"], ["偶尔送个不贵重的小礼物", "积极关注对方生活状态，找机会给予帮助", "给TA买一些爱吃的美食"], ["一起走在大街上，可以主动挽着TA的手臂", "两个人看电影时，可以把头倚在对方的肩膀上", "合适的时机，可以尝试握住TA的手"], ["尝试一下不同的妆容风格，或穿衣风格", "提前为TA准备爱吃的早饭", "一起去游乐园，尝试不同的游玩项目", "在特殊的日子，送TA一份有心意的礼物"], ["合适的时机聊聊彼此的近期的工作、学习经历", "与TA分享你遇到过的有趣的事", "带上TA一起参加朋友聚会", "分享彼此的生活情绪", "可以试着共同养一只宠物"], ["适当温柔地关心对方，避免采用说教的方式", "适当玩笑，让交流的氛围更加轻松", "挑一个对方感兴趣的话题，试着去展开分享彼此观点", "夸奖TA的想法或观点，增强交流分享的动力", "给对方起一个合适的昵称"], ["避免去刨根问底，不要带给TA很大的压力", "提升自身的学识能力，增加吸引力"], ["适当表露自己内心的烦恼或心事"], ["主动给TA一个紧紧的拥抱，温柔的亲吻", "挑一个TA喜欢的目的地，来一场属于两个人的旅行", "对于TA的亲密举动给予积极的回应"], ["避免轻易做承诺，但答应过的事一定要完成", "不要一味的让对方付出，需要适当的给予回馈"], ["把握撒娇或者作的尺度，不要用力过度", "合适的时机让TA了解你的家庭背景", "避免刻意掩盖自身缺点，试着用自嘲的方式来表露", "不要总把一些不满的情绪刻意隐藏，可以有适当的发泄"], ["在你们的纪念日，准备惊喜，讲讲往日相处时的幸福瞬间", "向TA表露你对于彼此未来的美好愿景与规划", "培养彼此间的默契，可以是简单的动作，也可是思维上的一致"], ["不逃避所面临的问题，试着表露彼此真实想法", "不要太过敏感，避免胡思乱想，互相猜忌"], ["第一时间感谢TA为你做的任何事情", "找合适的机会犒劳TA的付出，买份礼物、请顿大餐"], ["向对方说一声“我爱你”", "合适的时机，告诉对方“亲爱的，我为你感到骄傲”", "交流时，对于TA的想法，不要轻易打断去做评价批评", "告诉TA“你对我而言非常重要，甚至胜于一切”", "发现TA累的时候，及时上前安慰，“亲爱的，我能为你做些什么，能让你感觉好一些？”"], ["相处时深情抱住TA，持续10秒钟以上", "不忘给TA一个早安吻、晚安吻或见面吻", "坐在一起时，可以互相靠着对方"], ["对TA为你做的一件事表示赞赏、肯定或感激", "让对方知道自己最信任的人就是TA"], ["试着都不玩手机，花一段时间与TA独处", "来一场只属于两个人的长途旅行", "找个你们平时不常做的活动，一起完成一次"], ["为TA写一份爱的便笺或书信", "在TA不知情的时候，带一样TA最喜欢吃的东西", "准备一份TA想要很久但一直没有舍得买的东西作为礼物"], ["帮TA洗洗衣服，换换床单，打扫一下房间", "为TA精心准备一次丰盛的晚餐", "为了TA，做一件你平时不爱做但TA非常喜欢的事"], ["避免不合理的挑剔，觉得自己更胜一筹，而抓住TA的缺点不放", "避免草率的做出负面评价，不要轻易把问题原因直接归咎于TA", "不要逃避，避免在沟通时沉默、走开，不愿意就问题进行讨论", "避免表现过于傲慢，不要在TA犯错的时候小题大做，不愿宽恕", "不要做监视对方的行为，需要留一些私人空间"], ["试着放下内心强烈的自我防御，去认可对方，去做出一些自我调整与改变", "试着让步，退回到与TA平等的状态上，给予双方平等沟通的权利", "不要为自己免责，有错误也需要承认", "不要忽视对方的看法，只顾自身感受"], ["避免使用贬低的称呼，或者恶劣的态度语气与TA交流", "感谢TA努力对情感做出的表达，哪怕显得笨拙，也不要嘲笑"], ["感谢TA努力对情感做出的表达，哪怕显得笨拙，也不要嘲笑", "试着培养共同的兴趣爱好，周末一同去参加"], ["试着在公共场合或社交媒体上秀恩爱", "经常性地直接表达“我爱你”之类的甜言蜜语", "认真对待TA喜欢的事物，尝试理解他的需求", "肯定TA的负面情绪，在TA难过、愤怒、挫败时感受到你的支持和依靠"], ["试着共享彼此的社交，邀请彼此的朋友、亲人，并介绍互相认识", "试着去共同承担一些责任"]];

    var direction = [];
    var advice = [];
    var user_sex = document.getElementById("user_sex").value;
    if (user_sex == "男") {
        advice = male_advice;
    } else {
        advice = female_advice;
    }
    //清除旧有或历史
    var temp = document.getElementById("advice_details");
    for (var j = temp.children.length - 1; j >= 0; j--) {
        temp.children[j].remove();
    }
    //增加
    for (var i = 0; i < advice[x - 1].length; i++) {
        // 循环创建opt元素
        var opt = document.createElement("option");
        opt.value = advice[x - 1][i];
        opt.text = advice[x - 1][i];
        temp.appendChild(opt);
    }
}

jQuery.validator.addMethod("isNotDefaultNone", function (value, element) {
    var tel = "请选择";
    alert(value);
    return value != tel;
}, "");
