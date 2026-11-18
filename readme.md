### pip install
```bash
argparse
kimimaro
navis 
numpy 
pandas
caveclient
cloud-volume
```
### Skeletonise multiple segments together

```bash
python skeletonize_modular.py --ids 720575940407157162 720575940405104379 720575940405307349 \ 720575940405552659 720575940405594319 720575940405795172 720575940405803046 720575940406483996 \ 720575940406488460 720575940406683436 720575940406807915 720575940406808427 720575940407022582 \ 720575940407425991 720575940407694958 720575940408389592 720575940408775396 720575940408912632 \ 720575940410237440 720575940410621695 720575940415400896 720575940415570975 \
        --datastack zlatic_octo-2_datastack \  # pass your own stack
        --mip 4 \ # do not go below this mip. You can use mip=3, will take more time
        --const 10 \
        --pdrf-exponent 2 \
        --scale 1 \
        --smooth-window 2 \
        --resample 128 \
        --output-dir ./skeletons_nadia_13jul26 \ # make folder first on disk to save skels
        --coord-scale 128  # changing mip changes coord-scale. Logic: mip=4, 2^4 * 8 (vox res) = 128
```

These are segment IDs of your choice: `720575940407157162`

### Importing Skeletons into CATMAID
Follow the `import_skels_into_catmaid.py` script to upload skeletons to your own CATMAID instance.
Make sure you use your own project for this and you have sufficient permissions to use the CATMAID API.

