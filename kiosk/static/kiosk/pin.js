$(document).ready(function(){
   $('#prompt').children('span').mousedown(
       function(){
           $(this).addClass('active');
   }).mouseup(function(){
       $(this).removeClass('active');})
       .click(function(){
           $('#pin').removeClass('invisible');
          $('#pin').addClass('visible');
       });
});

(function () {
	var input = '',
	correct = '0440';

	var dots = document.getElementsByClassName('dot'),
	numbers = document.getElementsByClassName('number');
	dots = Array.from(dots);
	numbers = Array.from(numbers);

	var numbersBox = document.getElementsByClassName('numbers')[0];
	$(numbersBox).on('click', '.number', function (evt) {
		var number = $(this);

		number.addClass('grow');
		input += number.text();
		$(dots[input.length - 1]).addClass('active');

		if (input.length >= 4) {
			if (input !== correct) {
				dots.forEach(function (dot) {return $(dot).addClass('wrong');});
			} else
			{
				dots.forEach(function (dot) {return $(dot).addClass('correct');});
				$('#pin').addClass('success');
				setTimeout('window.location = \'/portal/\';', 500);

			}
			setTimeout(function () {
				dots.forEach(function (dot) {return dot.className = 'dot';});
				input = '';
			}, 900);
			setTimeout(function () {
			}, 1000);
		}
		setTimeout(function () {
			number.className = 'number';
		}, 1000);
	});
})();