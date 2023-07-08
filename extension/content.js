chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'downloadVideo') {
        var videoUrl = window.location.href;
    }
});