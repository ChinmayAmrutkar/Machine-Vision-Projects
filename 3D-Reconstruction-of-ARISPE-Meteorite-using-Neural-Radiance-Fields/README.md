# 3D Reconstruction of ARISPE Meteorite using Neural Radiance Fields (NeRF Studio)

Welcome to the repository for our project on **3D scene reconstruction** using Neural Radiance Fields (NeRF) techniques.  
In this project, we reconstructed a real-world object — the **ARISPE meteorite** specimen displayed at **Arizona State University (ASU)** — using **NeRF Studio** and compared three different NeRF methods.

---

## 📚 Project Overview

This project involves:
- Capturing a real-world dataset of a meteorite at ASU.
- Preprocessing using **Metashape** for camera pose estimation.
- Training three NeRF models:
  - **Instant-NGP**
  - **Nerfacto**
  - **TensoRF**
- Performing **qualitative analysis** to compare reconstruction quality.

The goal was to explore NeRF-based 3D modeling workflows and evaluate their effectiveness for real-world dataset challenges.

---

## 📸 Dataset Collection

- **55 images** were captured around the ARISPE meteorite in a **360° sweep**.
- Images were taken at varying heights and angles to maximize coverage and overlap.
- Camera poses were estimated using **Agisoft Metashape**, and sparse point clouds were generated.
- Poses were exported as `.xml` and converted to `transforms.json` compatible with NeRF Studio.

Sample captured images:

![Sample Image](images/sample_image.jpg)

Sparse cloud and camera poses:

![Sparse Cloud](images/sparse_cloud.jpg)

---

## 🛠 Reconstruction Methods

We trained and compared the following models:

### 1. Instant-NGP
- Training Time: **~2 minutes** on NVIDIA RTX 3050 GPU
- Extremely fast convergence using multiresolution hash grids.
- Surface structure reconstructed well.
- Minor blurring observed in fine features (e.g., text on the black plate).

### 2. Nerfacto
- Training Time: **~16 minutes**
- Produced the **highest reconstruction quality**.
- Finer surface details and text on the ARISPE information plate were **readable**.
- Background and transparent surfaces (like glass) reconstructed well.

### 3. TensoRF
- Training Time: **~92 minutes**
- Captured the basic structure, but significant **noise artifacts** appeared.
- Fine details and text were less accurately modeled compared to Nerfacto.

---

## 🧠 Qualitative Comparison

| Parameter                | Instant-NGP                         | Nerfacto                                  | TensoRF                                  |
|---------------------------|--------------------------------------|-------------------------------------------|------------------------------------------|
| Training Time             | 2 minutes                           | 16 minutes                                | 92 minutes                               |
| Reconstruction Quality    | Moderate                            | High                                      | Average                                  |
| Observations              | Moderate surface detail, noisy background, blurred fine text | Highly detailed, clean background, readable fine text | Scene captured, but heavy noise artifacts and unreadable text |

---

## 📝 Conclusion

- **Nerfacto** achieved the best balance between training speed and reconstruction quality.
- **Instant-NGP** is excellent for fast prototyping but struggles with fine details.
- **TensoRF**, while promising theoretically, was sensitive to noise in this real-world dataset.

The experiment highlights the importance of choosing the right NeRF model based on the reconstruction task requirements.

---

## 📂 Repository Structure

/images/ # Contains sample dataset images and sparse cloud visualizations /outputs/ # Trained models outputs (optional, if included) /paper/ # Final conference-style paper (PDF) /code_snippets/ # Code snippets used during training README.md # Project overview
---

## 🔗 References

- [NerfStudio Documentation](https://docs.nerf.studio/)
- [Instant-NGP (NVIDIA)](https://github.com/NVlabs/instant-ngp)
- [Nerfacto (Nerfstudio)](https://docs.nerf.studio/nerfology/methods/nerfacto.html)
- [TensoRF (Official GitHub)](https://github.com/apchenstu/TensoRF)
- [Metashape by Agisoft](https://www.agisoft.com/)

---

<p align="center">
  <em>Built with ❤️ for 3D Vision Research and Learning</em>
</p>
