"use strict";

document.addEventListener("DOMContentLoaded", () => {
  // ===== Adjust Hero Padding =====
  const nav = document.querySelector("nav");
  const hero = document.querySelector(".video-container");
  if (nav && hero) {
    hero.style.paddingTop = `${nav.offsetHeight}px`;
  }

  // ===== Sounds =====
  const hoverSound = document.getElementById("hoverSound");
  const clickSound = document.getElementById("clickSound");

  const experienceItems = document.querySelectorAll(".experience-item");
  experienceItems.forEach(item => {
    item.addEventListener("mouseenter", () => {
      if (hoverSound) {
        hoverSound.currentTime = 0;
        hoverSound.play();
      }
    });
    item.addEventListener("click", () => {
      if (clickSound) {
        clickSound.currentTime = 0;
        clickSound.play();
      }
    });
  });

  // ===== Animate Hero on Load (10s delay) =====
  setTimeout(() => {
    const heroContent = document.querySelector(".hero-content");
    if (heroContent) heroContent.classList.add("animate");
  }, 10000);

  // ===== Smooth Scroll =====
  const scrollToSection = (event) => {
    event.preventDefault();
    const targetId = event.target.getAttribute("href")?.slice(1);
    const targetElement = document.getElementById(targetId);

    if (targetElement) {
      window.scrollTo({
        top: targetElement.offsetTop - 50,
        behavior: "smooth",
      });
    }
  };

  document.querySelectorAll(".nav-button").forEach((anchor) => {
    anchor.addEventListener("click", scrollToSection);
  });

  // ===== Job Experience Section =====
  const heroSection = document.getElementById("hero-section");
  const jobLinks = document.querySelectorAll(".year-job-list a");

  const jobDescriptions = {
    electrician: `<h1>1 Year Electrician</h1><p>With one year of experience as an electrician, I have developed a strong foundation in electrical systems and troubleshooting...</p>`,
    multimedia: `<h1>3 Years Multimedia Specialist</h1><p>As a multimedia specialist, I have worked on video editing, graphic design, and content creation...</p>`,
    "graphic-designer": `<h1>6 Months Graphic Designer</h1><p>My experience as a graphic designer includes creating visuals for branding, social media, and marketing materials...</p>`,
    "it-support": `<h1>6 Months IT Tech Support</h1><p>Providing technical support, troubleshooting network issues, and assisting users with hardware and software problems...</p>`,
    "admin-specialist": `<h1>1 Year and 5 Months Administrative Specialist</h1><p>Managing office operations, handling documentation, and ensuring smooth administrative processes...</p>`,
  };

  const updateHero = (content) => {
    if (heroSection) {
      heroSection.innerHTML = content;
      heroSection.classList.remove("hidden");
    }
  };

  jobLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      const jobKey = link.getAttribute("data-job");
      if (jobDescriptions[jobKey]) {
        updateHero(jobDescriptions[jobKey]);
      }
    });
  });
});
