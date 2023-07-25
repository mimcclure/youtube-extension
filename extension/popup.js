//button click event

document.addEventListener('DOMContentLoaded', function() {
    var downloadButton = document.getElementById('downloadButton');
    downloadButton.addEventListener('click', function() {

      //Get all tabs that are active and currently open and give the action of being able to download
      chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        var activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, { action: 'downloadVideo' });
      })
    })
  })