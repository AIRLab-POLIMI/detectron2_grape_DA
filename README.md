# Custom Mask RCNN for Surgical Fine-tuning 
We apply "surgical fine-tuning" (Lee et al., 2023) to the MaskRCNN pipeline of the detectron2 library (Wu et al., 2019)
by modifying the configuration of ResNet backbones in detectron2.

## License

Detectron2 is released under the [Apache 2.0 license](LICENSE).

## References 

```BibTeX
@misc{wu2019detectron2,
  author =       {Yuxin Wu and Alexander Kirillov and Francisco Massa and
                  Wan-Yen Lo and Ross Girshick},
  title =        {Detectron2},
  howpublished = {\url{https://github.com/facebookresearch/detectron2}},
  year =         {2019}
}
```

```BibTeX
@inproceedings{lee2023surgical,
  title={Surgical Fine-Tuning Improves Adaptation to Distribution Shifts},
  author={Lee, Yoonho and Chen, Annie S and Tajwar, Fahim and Kumar, Ananya and Yao, Huaxiu and Liang, Percy and Finn, Chelsea},
  booktitle={Proceedings of the The Eleventh International Conference on Learning Representations (ICLR)},
  year={2023}
}
```
