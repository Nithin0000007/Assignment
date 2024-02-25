

document.addEventListener("DOMContentLoaded", function() {
  const uploadButton = document.getElementById('uploadButton');
  const fileInput = document.getElementById('fileInput');
  const outputDiv = document.getElementById('output');

  uploadButton.addEventListener('click', function() {
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'C:\\python_work\\Assignments\\Assignment6\\dataExtraction.py', true);
    xhr.onload = function() {
      if (xhr.status === 200) {
        outputDiv.textContent = xhr.responseText;
      } else {
        outputDiv.textContent = 'Error processing file';
      }
    };

    xhr.send(formData);
  });
});
