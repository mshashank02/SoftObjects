
### `objects/`
Each object folder typically contains:
- `surf/*.obj` — surface triangle mesh
- `tet_*/tetwild_out*.msh` — tetrahedral mesh in **Gmsh v2.2** format (often **binary**)
- `*.xml` — MuJoCo model(s) that load the tetra mesh using `<flexcomp type="gmsh" ...>`

### `fTetWild/`
Source code for **fTetWild** (“Fast Tetrahedral Meshing in the Wild”). See `fTetWild/README.md` for full details and options.

## Requirements

- **CMake** + a **C++ compiler** (for building `fTetWild`)
- **GMP** development headers/libraries (dependency of `fTetWild`)
- **MuJoCo** (for running the XML examples)

> Note: Some provided XML files use **absolute paths** (e.g. `/home/...`). You’ll likely need to edit them to use paths on your machine (see below).

## Quickstart

### 1) Build fTetWild

```bash
cd fTetWild
mkdir -p build
cd build
cmake ..
make -j

# sanity check
./FloatTetwild_bin --help

./fTetWild/build/FloatTetwild_bin \
  -i objects/large_1/surf/large_1.obj \
  -o objects/large_1/tet_coarse/tetwild_out_.msh \
  --lr 0.05 \
  --epsr 1e-3
