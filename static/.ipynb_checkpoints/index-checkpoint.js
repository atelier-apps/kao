
const messageForSelectFile = '画像を選択する'
const messageForReselectFile = '画像を選びなおす'
const default_image = './static/img/main.png'
const id_upload_btn = 'uploadBtn'
const id_select_btn = 'selectFile'
const id_upload_text = 'uploadText'
const id_file = 'file'
const id_image = 'image'
const id_default='id_default'
const id_selected='id_selected'

window.onload = function () {
    
    $("#"+id_image).attr("src",default_image);
    $("#"+id_upload_btn).attr("disabled",true);
    $("#"+id_select_btn).addClass("main");
    $("#"+id_upload_text).text(messageForSelectFile);
}

function isSelected() {
    const file = document.getElementById(id_file)
    if (file.value === '') {
        $("#"+id_default).removeClass("hidden");
        $("#"+id_selected).addClass("hidden");
        $("#"+id_upload_btn).attr("disabled",true);
        $("#"+id_select_btn).addClass("main");
        $("#"+id_upload_text).text(messageForSelectFile);
        $("#"+id_image).attr("src",default_image);
    } else {
        $("#"+id_default).addClass("hidden");
        $("#"+id_selected).removeClass("hidden");
        $("#"+id_upload_btn).attr("disabled",false);
        $("#"+id_select_btn).removeClass("main");
        $("#"+id_upload_text).text(messageForReselectFile);
        $("#"+id_image).attr("src",window.URL.createObjectURL(file.files[0]));
    }
}