$(document).ready(function () {
    $('.selectpicker').selectpicker({
        virtualScroll: true, // Enable virtual scrolling
        virtualScrollIncrement: 20, // Number of options to load on each scroll
        virtualScrollItemHeight: 20, // Height of each option item
        size: 5 // Number of initially visible options
    });
});
