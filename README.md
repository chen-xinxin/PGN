## Part Grouping Network (PGN)
记录怎么用PGN获得分析图


### Crowd Instance-level Human Parsing (CIHP) Dataset

The PGN is trained and evaluated on our [CIHP dataset](https://lip.sysuhcp.com/) for isntance-level human parsing.  Please check it for more model details. The dataset is also available at [google drive](https://drive.google.com/drive/folders/0BzvH3bSnp3E9QjVYZlhWSjltSWM?resourcekey=0-nkS8bDVjPs3bEw3UZW-omA&usp=sharing) and [baidu drive](http://pan.baidu.com/s/1nvqmZBN).

### Pre-trained models

We have released our trained models of PGN on CIHP dataset at [google drive](https://drive.google.com/open?id=1Mqpse5Gen4V4403wFEpv3w3JAsWw2uhk).

### Inference
1. Download the pre-trained model and store in $HOME/checkpoint.
2. Prepare the images and store in $HOME/datasets.
3. Run test_pgn.py.
4. The results are saved in $HOME/output
5. Evaluation scripts are in $HOME/evaluation. Copy the groundtruth files (in _Instance_ids_ folder) into $HOME/evaluation/Instance_part_val before you run the script.

### Training
1. Download the pre-trained model and store in $HOME/checkpoint.
2. Download CIHP dataset or prepare your own data and store in $HOME/datasets.
3. For CIHP dataset, you need to generate the edge labels and left-right flipping labels (optional). We have provided a script for reference.
4. Run train_pgn.py to train PGN.
5. Use test_pgn.py to generate the results with the trained models.
6. The instance tool is used for instance partition process from semantic part segmentation maps and instance-aware edge maps, which is written in MATLAB.


