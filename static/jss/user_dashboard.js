document.addEventListener('DOMContentLoaded', function() {
    var url = '{{ latest_pdf.file.url }}';  // Update this with your PDF URL

    // Asynchronous download of PDF
    pdfjsLib.getDocument(url).promise.then(function(pdf) {
        console.log('PDF loaded');

        // Fetch the first page
        pdf.getPage(1).then(function(page) {
            console.log('Page loaded');

            var scale = 1.5;
            var viewport = page.getViewport({ scale: scale });

            // Prepare canvas using PDF page dimensions
            var canvas = document.createElement('canvas');
            var context = canvas.getContext('2d');
            canvas.height = viewport.height;
            canvas.width = viewport.width;

            // Append canvas to the div
            document.getElementById('pdf-container').appendChild(canvas);

            // Render PDF page into canvas context
            var renderContext = {
                canvasContext: context,
                viewport: viewport
            };
            page.render(renderContext).promise.then(function() {
                console.log('Page rendered');
            });
        });
    }, function(reason) {
        console.error(reason);
    });
});
