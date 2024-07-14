document.querySelector('.menu-toggle').addEventListener('click', function() {
    document.querySelector('nav ul').classList.toggle('show');
    });
    let slideIndex = 0;

    function showTestimonials() {
    let testimonials = document.getElementsByClassName("testimonial");
    for (let i = 0; i < testimonials.length; i++) {
        testimonials[i].classList.remove("active"); // Remove active class from all testimonials
    }
    slideIndex++;
    if (slideIndex > testimonials.length) {slideIndex = 1}
    testimonials[slideIndex-1].classList.add("active"); // Add active class to the next testimonial
    }
    document.querySelector('.prev-slide').addEventListener('click',() => {
        showTestimonials(-1);
    });
    document.querySelector('.next-slide').addEventListener('click',() => {
        showTestimonials(-1);
    });


    showTestimonials();


