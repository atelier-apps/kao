
const messageForSelectFile = '画像を選択する'
const messageForReselectFile = '画像を選びなおす'
const default_image = './static/uploads/default.jpg'
const id_upload_btn = 'uploadBtn'
const id_upload_text = 'uploadText'
const id_file = 'file'
const id_image = 'image'
const id_result = 'result'

window.onload = function () {
    document.getElementById(id_upload_btn).disabled = true
    document.getElementById(id_upload_text).innerText = messageForSelectFile
    if (!location.pathname.includes('post')) {
        document.getElementById(id_result).style.display = "none"
    }
}

function isSelected() {
    const file = document.getElementById(id_file)
    if (file.value === '') {
        document.getElementById(id_upload_btn).disabled = true
        document.getElementById(id_upload_text).innerText = messageForSelectFile
        document.getElementById(id_image).src = default_image
    } else {
        document.getElementById(id_upload_btn).disabled = false
        document.getElementById(id_upload_text).innerText = messageForReselectFile
        document.getElementById(id_image).src = window.URL.createObjectURL(file.files[0])
    }
    document.getElementById(id_result).style.display = "none"
}