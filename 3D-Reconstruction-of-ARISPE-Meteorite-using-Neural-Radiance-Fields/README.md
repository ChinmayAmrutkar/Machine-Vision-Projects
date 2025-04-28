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

Sample captured image:

<p align="center">
  <img src="https://github.com/user-attachments/assets/c51e278f-3707-4046-93f8-5077211f3d4a" width="45%">
</p>

Sparse cloud and camera poses:

<p align="center">
  <img src="https://github.com/user-attachments/assets/cfb07033-bad7-4370-bb6c-ef56971674e7" width="45%">
</p>

---

## 🛠 Reconstruction Methods

We trained and compared the following models:

### 1. Instant-NGP
- Training Time: **~2 minutes** on NVIDIA RTX 3050 GPU
- Extremely fast convergence using multiresolution hash grids.
- Surface structure reconstructed well.
- Minor blurring observed in fine features (e.g., text on the black plate).

<p align="center">
  <img src="https://github.com/user-attachments/assets/ecf53340-8cf3-4775-bfa5-d0baf943639d" width="45%">
  <img src="https://github.com/user-attachments/assets/5cacf3b0-2388-4b3e-b1fc-76d28fcad75a" width="45%">
</p>

---

### 2. Nerfacto
- Training Time: **~16 minutes**
- Produced the **highest reconstruction quality**.
- Finer surface details and text on the ARISPE information plate were **readable**.
- Background and transparent surfaces (like glass) reconstructed well.

<p align="center">
  <img src="https://github.com/user-attachments/assets/c852d332-c05c-4a7d-a6b4-dcc6b90da47e" width="45%">
  <img src="https://github.com/user-attachments/assets/8b5149f2-fc01-4ce4-9059-9b2069ec5d7e" width="45%">
</p>

---

### 3. TensoRF
- Training Time: **~92 minutes**
- Captured the basic structure, but significant **noise artifacts** appeared.
- Fine details and text were less accurately modeled compared to Nerfacto.

<p align="center">
  <img src="https://github.com/user-attachments/assets/2bed5715-16a7-4ecb-8f3a-6a92f96f3ec6" width="45%">
  <img src="https://github.com/user-attachments/assets/9b1d92f2-6a57-41e1-91d0-8a752cdcad4c" width="45%">
</p>

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

## 📄 More Information

For a detailed technical analysis, methodology, and complete results, please refer to the full project [paper](https://github.com/ChinmayAmrutkar/Machine-Vision-Projects/blob/main/3D-Reconstruction-of-ARISPE-Meteorite-using-Neural-Radiance-Fields/Efficient_3D_Scene_Modeling_with_Instant_NGP__Nerfacto__and_TensoRF__A_Case_Study_on_the_ARISPE_Meteorite.pdf) included in this repository.

---

## 🔗 References

- [NerfStudio Documentation](https://docs.nerf.studio/)
- [Instant-NGP (NVIDIA)](https://github.com/NVlabs/instant-ngp)
- [Nerfacto (Nerfstudio)](https://docs.nerf.studio/nerfology/methods/nerfacto.html)
- [TensoRF (Official GitHub)](https://github.com/apchenstu/TensoRF)
- [Metashape by Agisoft](https://www.agisoft.com/)

---

## 📜 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this work, provided that proper credit is given.

For more details, see the [LICENSE]([LICENSE](https://github.com/ChinmayAmrutkar/Machine-Vision-Projects/blob/main/3D-Reconstruction-of-ARISPE-Meteorite-using-Neural-Radiance-Fields/LICENSE.txt)) file.

---

<p align="center">
  <em>Built with ❤️ for 3D Vision Research and Learning</em>
</p>
