---
title: "Research"
permalink: /research/
layout: single
author_profile: true
classes: wide
excerpt: "Publications and selected research projects by Chendong Xin."
---

<div class="research-list" data-research-list>
  <div class="research-filter" role="group" aria-label="Filter research items">
    <button class="research-filter__button is-active" type="button" data-filter="major" aria-pressed="true">Major</button>
    <button class="research-filter__button" type="button" data-filter="all" aria-pressed="false">Show all</button>
  </div>

  <article class="research-item" data-scope="major">
    <p class="research-item__type">Publication · 2025</p>
    <h2><a href="https://compliant-residual-dagger.github.io/">Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections</a></h2>
    <p class="research-item__authors">Xiaomeng Xu*, Yifan Hou*, <strong>Chendong Xin</strong>, Zeyi Liu, and Shuran Song</p>
    <p class="research-item__venue"><strong>NeurIPS 2025</strong> · Human-to-Robot Workshop at CoRL 2025, Best Paper</p>
    <p class="research-item__links"><a href="https://compliant-residual-dagger.github.io/">Website</a><span>·</span><a href="https://arxiv.org/abs/2506.16685">Paper</a><span>·</span><a href="https://github.com/yifan-hou/cr-dagger">Code</a></p>
    <p class="research-item__tldr"><strong>TL;DR:</strong> A compliant intervention interface and residual policy enable robots to learn precise, contact-rich manipulation from minimal human correction data.</p>
  </article>

  <article class="research-item" data-scope="major">
    <p class="research-item__type">Publication · 2025</p>
    <h2><a href="https://mingrui-yu.github.io/retargeting/">Analyzing Key Objectives in Human-to-Robot Retargeting for Dexterous Manipulation</a></h2>
    <p class="research-item__authors"><strong>Chendong Xin*</strong>, Mingrui Yu*, Yongpeng Jiang, Zhefeng Zhang, and Xiang Li</p>
    <p class="research-item__venue"><strong>IEEE Robotics and Automation Practice, 2025</strong> · ICRA 2025 Workshop on Handy Moves</p>
    <p class="research-item__links"><a href="https://mingrui-yu.github.io/retargeting/">Website</a><span>·</span><a href="https://arxiv.org/pdf/2506.09384">Paper</a><span>·</span><a href="https://github.com/Mingrui-Yu/retargeting">Code</a></p>
    <p class="research-item__tldr"><strong>TL;DR:</strong> A unified formulation and real-world ablation study reveal which objectives matter most when retargeting human hand motion to robot hands.</p>
  </article>

  <article class="research-item" data-scope="all" hidden>
    <p class="research-item__type">Competition &amp; Workshop Paper · 2025</p>
    <h2><a href="https://drive.google.com/file/d/1JeVUZnuA85vtoRfEPpvAHd7XtUSx0bg3/view">Hybrid Gripper and Adaptive Strategy for Robust Grasping in Clutter: RGMC Champion Solution</a></h2>
    <p class="research-item__authors">Shihefeng Wang*, <strong>Chendong Xin*</strong>, Zhefeng Zhang, Gongrui Ma, and Xiang Li</p>
    <p class="research-item__venue"><strong>1st Place, ICRA 2025 RGMC Picking-in-Clutter Track</strong> · IROS 2025 Workshop on Benchmarking via Competitions in Robotic Grasping and Manipulation</p>
    <p class="research-item__links"><a href="https://drive.google.com/file/d/1JeVUZnuA85vtoRfEPpvAHd7XtUSx0bg3/view">Workshop Paper</a><span>·</span><a href="https://sites.google.com/view/rgmc2025">Competition</a></p>
    <p class="research-item__tldr"><strong>TL;DR:</strong> A hybrid end effector and adaptive decluttering strategy form a robust perception-to-execution system for picking objects from dense clutter.</p>
  </article>

  <p class="research-note">* Equal contribution.</p>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  var list = document.querySelector("[data-research-list]");
  if (!list) return;

  var buttons = list.querySelectorAll("[data-filter]");
  var items = list.querySelectorAll("[data-scope]");

  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      var filter = button.getAttribute("data-filter");

      buttons.forEach(function (candidate) {
        var active = candidate === button;
        candidate.classList.toggle("is-active", active);
        candidate.setAttribute("aria-pressed", active ? "true" : "false");
      });

      items.forEach(function (item) {
        item.hidden = filter === "major" && item.getAttribute("data-scope") === "all";
      });
    });
  });
});
</script>
