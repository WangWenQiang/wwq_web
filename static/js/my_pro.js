/**
 * Created by wangwenqiang on 2017/12/27.
 */

//ajax test
function DoAjax() {
    var tmp = $('#www').val();
    var sample_id = $('#sampleID').val();
    $.ajax({
        url: "/fresh",
        async : false,
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        type: "POST",
        data: {operate: tmp, sample_id: sample_id},
        success: function (arg) {
            var obj = jQuery.parseJSON(arg);
            $('#eee').val(obj.operate);
        }
    })
}
//重置被选中的style
function reset_radio_style() {
    var all_radio = document.getElementsByTagName("label");
    for (var a = 0; a < all_radio.length; a++) {
        all_radio[a].style.color = "";
        all_radio[a].style.fontweight = "";
        all_radio[a].style.border = "";
    }
}
//保存打分-ajax-from方法
function saveScore() {
    alert($("#myForm").elem);
    var options = {
        url: "/test",
        success: function () {
            alert('123');
            reset_radio_style();
            show_commit();
        },
        error: function () {
            alert("error");
            reset_radio_style();
            show_commit();
        },
        clearForm: true,
        timeout: 100000
    };
    $("#myForm").ajaxSubmit(options);
}
//保存打分-一般方法
function submit_all() {
    document.myForm.action = "/test";
    document.myForm.submit();
}
//只显示打分按钮
function show_score() {
    $("#score_btn").show();
    $("#commit_btn").hide();
    $("#finish_btn").hide();
}
//显示行为按钮
function show_commit() {
    $("#score_btn").hide();
    $("#commit_btn").show();
    $("#finish_btn").show();
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
    var label_id = 'label_' + radio_id;
    for (var k = 0; k < line_radio.length; k++) {
        var tmp_radio = line_radio[k];
        if (tmp_radio.id == label_id) {
            tmp_radio.style.color = "yellow";
            tmp_radio.style.fontweight = "bold";
            tmp_radio.style.border = "0.05px dashed";
        } else {
            tmp_radio.style.color = "";
            tmp_radio.style.fontweight = "";
            tmp_radio.style.border = "";
        }
    }
}
