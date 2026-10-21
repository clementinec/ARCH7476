# Vibes vs Evidence Image Set

These local 16:9 PNGs support the Week 1 "Sometimes Evidence Is Just Vibes" slide sequence.

The intended teaching pattern is:

1. show a persuasive image;
2. ask students to state the vibe claim;
3. reveal why it is not evidence yet;
4. reveal what evidence would strengthen the claim.

## Current Image Direction

These were rebuilt after the first procedural placeholder set looked too illustrated. The current version uses realistic, picturesque source photographs cropped into stable 1600x900 PNGs.

### `restaurant-vibe.png`

Realistic, polished restaurant interior with strong architectural atmosphere. It is visually seductive and spatially rich, but still does not prove layout performance, service flow, acoustics, or actual occupancy patterns.

Source: Eater / Vox Media image URL listed in [_revamp/build_vibe_images.py](../../../_revamp/build_vibe_images.py).

### `phone-camera-vibe.png`

Realistic smartphone camera-preview image with a scenic view. It looks like persuasive product-ad evidence, but it does not prove camera performance, failure cases, compression behavior, or controlled comparison quality.

Source: Le Livre Scolaire image URL listed in [_revamp/build_vibe_images.py](../../../_revamp/build_vibe_images.py).

### `calm-route-vibe.png`

Realistic French streetscape at blue hour with trees, lamps, and a quiet road. It suggests calm and safety, but does not prove pedestrian risk, lighting sufficiency, conflict rate, or user perception across time.

Source: The Roads Beyond image URL listed in [_revamp/build_vibe_images.py](../../../_revamp/build_vibe_images.py).

### `green-facade-vibe.png`

Realistic greenery-heavy building facade. It visually implies sustainability and biophilic performance, but does not prove heat gain, irrigation load, biodiversity value, embodied carbon, or maintenance viability.

Source: Matador Network image URL listed in [_revamp/build_vibe_images.py](../../../_revamp/build_vibe_images.py).

## Rebuild

Run:

```bash
python3 _revamp/build_vibe_images.py
```
