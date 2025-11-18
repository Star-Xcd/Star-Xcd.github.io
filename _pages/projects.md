---
title: "Projects"
permalink: /projects/
layout: single
author_profile: true
classes: wide
toc: true
toc_label: "Projects"
toc_icon: "cog"
---

<!-- ## Research Projects -->

### Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections 

**Duration:** 06/2025 - 09/2025  
**Advisor:** Prof. Shuran Song  
**Lab:** [Robotics and Embodied Artificial Intelligence Lab](https://real.stanford.edu), Stanford University   
*This is the project I participate in during my internship at Stanford REALab.*  

**TL;DR**: Improving contact-rich manipulation with a compliant residual policy learned from on-policy delta human correction.

We address key challenges in Dataset Aggregation (DAgger) for real-world contact-rich manipulation: how to collect informative human correction data and how to effectively update policies with this new data. We introduce Compliant Residual DAgger (CR-DAgger), which contains two novel components: 1) a Compliant Intervention Interface that leverages compliance control, allowing humans to provide gentle, accurate delta action corrections without interrupting the ongoing robot policy execution; and 2) a Compliant Residual Policy formulation that learns from human corrections while incorporating force feedback and force control. Our system significantly enhances performance on precise contact-rich manipulation tasks using minimal correction data, improving base policy success rates by over 50% on two challenging tasks (book flipping and belt assembly) while outperforming both retraining-from-scratch and finetuning approaches. Through extensive real-world experiments, we provide practical guidance for implementing effective DAgger in real-world robot learning tasks.

### The 10th Robotics Grasping and Manipulation Competition (RGMC)

**Duration:** 02/2025 - 05/2025  
**Advisor:** Prof. Xiang Li  
**Lab:** [Intelligent Robotic Manipulation Lab](https://thu-irml.com), Department of Automation, Tsinghua University 

**TL;DR**: A perception-to-execution pipeline using a hybrid gripper to pick in clutter.

**We won the ICRA 2025 Robotic Grasping and Manipulation Competition (RGMC) “Picking from Clutter” track.** We tackle the challenge of sequential picking in dense clutter via developing a robotic system integrating a novel hybrid endeffector (including a parallel gripper, a suction cup and an electromagnet), a robust algorithm pipeline, and a pragmatic decluttering strategy. The system’s efficacy was benchmarked in a real-world, on-site competition, where it secured first place, outperforming other systems in both robustness and efficiency.

### Analyzing Key Objectives in Human-to-Robot Retargeting for Dexterous Manipulation

**Duration:** 01/2025 - 04/2025  
**Advisor:** Prof. Xiang Li  
**Lab:** [Intelligent Robotic Manipulation Lab](https://thu-irml.com), Department of Automation, Tsinghua University  
**Project Website:** [https://mingrui-yu.github.io/retargeting](https://mingrui-yu.github.io/retargeting)

**TL;DR**: A unified formulation and ablation study clarifying what matters in hand retargeting objectives.

Kinematic retargeting from human hands to robot hands is essential for transferring dexterity from humans to robots in manipulation teleoperation and imitation learning. However, due to mechanical differences between human and robot hands, completely reproducing human motions on robot hands is impossible. Existing works on retargeting incorporate various optimization objectives, focusing on different aspects of hand configuration. However, the lack of experimental comparative studies leaves the significance and effectiveness of these objectives unclear. This work aims to analyze these retargeting objectives for dexterous manipulation through extensive realworld comparative experiments. Specifically, we propose a comprehensive retargeting objective formulation that integrates intuitively crucial factors appearing in recent approaches. The significance of each factor is evaluated through experimental ablation studies on the full objective in kinematic posture retargeting and real-world teleoperated manipulation tasks. Experimental results and conclusions provide valuable insights for designing more accurate and effective retargeting algorithms for real-world dexterous manipulation.

<!-- ## Selected Course Projects -->

