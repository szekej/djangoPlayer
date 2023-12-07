document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('randomEpisode').addEventListener('click', function() {
    var totalEpisodesElement = document.getElementById('totalEpisodes');
    var stringValue = totalEpisodesElement.value;                           // get whole big string

    stringValue = stringValue.replace(/[\[\] ]/g, '');
    var availableEpisodes = stringValue.split(',');                         // convert this string to list of episodes

    var randomIndex = Math.floor(Math.random() * availableEpisodes.length); // get random episode
    var randomEpisodeNumber = availableEpisodes[randomIndex];

    window.location.href = '/player/video/' + randomEpisodeNumber + '/';    // go to page
    });
});