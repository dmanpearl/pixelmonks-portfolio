/* Carousel — minimal vanilla JS with slide animation */
(function () {
  const wrap = document.getElementById("carousel");
  if (!wrap) return;

  const slides = Array.from(wrap.querySelectorAll(".carousel-slide"));
  const dots = Array.from(document.querySelectorAll(".carousel-dots .dot"));
  const thumbs = Array.from(document.querySelectorAll(".thumb-strip .thumb"));
  const prevBtn = document.getElementById("carousel-prev");
  const nextBtn = document.getElementById("carousel-next");

  let current = 0;
  const ENTER_RIGHT = "carousel-slide--enter-right";
  const ENTER_LEFT = "carousel-slide--enter-left";

  function goTo(index, direction) {
    if (index === current) return;

    // Determine slide direction: 'right' = next, 'left' = prev
    const enterClass =
      direction === "prev" ? ENTER_LEFT : ENTER_RIGHT;

    // Hide current
    slides[current].classList.remove("carousel-slide--active");
    dots[current]?.classList.remove("dot--active");
    thumbs[current]?.classList.remove("thumb--active");

    current = (index + slides.length) % slides.length;

    // Animate in the new slide
    const entering = slides[current];
    entering.classList.remove(ENTER_RIGHT, ENTER_LEFT);
    entering.classList.add("carousel-slide--active", enterClass);

    entering.addEventListener(
      "animationend",
      () => entering.classList.remove(ENTER_RIGHT, ENTER_LEFT),
      { once: true }
    );

    dots[current]?.classList.add("dot--active");
    thumbs[current]?.classList.add("thumb--active");
  }

  prevBtn?.addEventListener("click", () => goTo(current - 1, "prev"));
  nextBtn?.addEventListener("click", () => goTo(current + 1, "next"));

  dots.forEach((dot) => {
    dot.addEventListener("click", () => {
      const target = Number(dot.dataset.target);
      goTo(target, target > current ? "next" : "prev");
    });
  });

  thumbs.forEach((thumb) => {
    thumb.addEventListener("click", () => {
      const target = Number(thumb.dataset.target);
      goTo(target, target > current ? "next" : "prev");
    });
  });

  /* Auto-advance every 6 s; pause on hover */
  let timer = setInterval(() => goTo(current + 1, "next"), 6000);
  wrap.addEventListener("mouseenter", () => clearInterval(timer));
  wrap.addEventListener("mouseleave", () => {
    timer = setInterval(() => goTo(current + 1, "next"), 6000);
  });
})();
