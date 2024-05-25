let stars = $(".rating .star");
let ratingValue = $(".rating input");
let ratingBtn = $("#rating-Btn");

stars.each(function (index1) {
    $(this).on('click', function () {
        ratingValue.val(index1 + 1);
        stars.each(function (index2) {
            if (index1 >= index2) {
                $(this).addClass("colored");
            } else {
                $(this).removeClass("colored");
            }
        });
    });
});

ratingBtn.on('click', function () {
    stars.removeClass("colored");
});