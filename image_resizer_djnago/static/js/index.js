// window.onload = initAll;
// window.alert();

// var resizeButton;
// function initAll() {
//     console.log(123);
//     resizeButton = document.getElementById('resize-btn-id');
//     resizeButton.onclick = Resize;
// }

// function Resize() {
//     var height = document.getElementById('height-id').value;
//     var width = document.getElementById('width-id').value;
//     var expected_file_size = document.getElementById('file-size-id').value;
//     var exten = document.getElementById('exten-id').value;
//     var img = document.getElementById('img-id').value;

//     console.log(height);
//     console.log(width);
//     console.log(expected_file_size);
//     console.log(exten);
//     console.log(img);

//     // $.ajax({
//     //     url: 'contact-us/subscribe/',
//     //     data: {
//     //         'email': email_id,
//     //         csrfmiddlewaretoken: '{{ csrf_token }}'
//     //     },
//     //     dataType: 'json',
    
//     //     success: function (data) {
//     //         if (data.is_taken) {
//     //             document.querySelector('.email-credentials').style.display = 'none';
//     //             document.querySelector('.mes').style.display = 'block';
//     //             document.getElementById('message-content').style.color = 'red';
//     //             document.getElementById('message-content').innerHTML = data.error_message; 
//     //         } else{
//     //             document.querySelector('.email-credentials').style.display = 'none';
//     //             document.querySelector('.mes').style.display = 'block';
//     //             document.getElementById('message-content').style.color = 'mediumseagreen';
//     //             document.getElementById('message-content').innerHTML = data.success_message;
//     //         }
//     //     }
//     // });
// }