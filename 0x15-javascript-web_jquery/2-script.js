const $head = $('header');
const $divRedHead = $('div#red_header');

$divRedHead.click(function () {
	$head.css({color: '#FF0000'});
});
