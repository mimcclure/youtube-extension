chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'downloadVideo') {
        var videoUrl = window.location.href;
        var requestData = { video_url: videoUrl };
        fetch('http://localhost:5000/download', {
            body: JSON.stringify(requestData)
        })
        .then(function(response) {
            return response.json()
        })
        .then(function(data) {
            console.log(data)
            console.log(response.status)
        })
    }
});