import tensorflow as tf
import tensorflow_datasets as tfds

# print(tfds.list_builders())
# data_dir = "~/tensorflow_datasets/downloads/manual"

config = tfds.translate.wmt.WmtConfig(
    version="0.0.6",
    language_pair=("de", "en"),
    subsets={
        tfds.Split.TRAIN: ["commoncrawl", "europarl_v7"],
        tfds.Split.VALIDATION: ["newstest2014"],
    },
)

builder = tfds.builder("wmt_translate", config=config)
print(builder.info.splits)
builder.download_and_prepare()
datasets = builder.as_dataset(as_supervised=True)
# print('datasets is {}'.format(datasets))


# # data_dir = "~/tensorflow_datasets/wmt_translate/0.0.1/downloads/manual"

# wmt_builder = tfds.builder("wmt_translate", config=config)
# print(wmt_builder.info)

# # wmt_builder = tfds.builder_from_directory(builder_dir=data_dir)
# # wmt_builder.download_and_prepare()
# datasets = wmt_builder.as_dataset()
# # print(datasets)



# config = tfds.translate.wmt.WmtConfig(
#     description="WMT translation task dataset.",
#     version="0.0.4",
#     language_pair=("de", "en"),
#     subsets={
#         tfds.Split.TRAIN: ["newscommentary_v14"],
#         tfds.Split.VALIDATION: ["newstest2014"],
#     }
# )

# builder = tfds.builder("wmt_translate", config=config)
# print(builder.info.splits)
# builder.download_and_prepare()
# datasets = builder.as_dataset(as_supervised=True)
# print('datasets is {}'.format(datasets))

# builder = tfds.builder("huggingface:wmt14")

# builder = tfds.builder("wmt_translate", config=config)
# print(builder.info)



# tfds.load(
#     name: str,
#     *,
#     split: Optional[Tree[splits_lib.SplitArg]] = None,
#     data_dir: Optional[str] = None,
#     batch_size: tfds.typing.Dim = None,
#     shuffle_files: bool = False,
#     download: bool = True,
#     as_supervised: bool = False,
#     decoders: Optional[TreeDict[decode.partial_decode.DecoderArg]] = None,
#     read_config: Optional[tfds.ReadConfig] = None,
#     with_info: bool = False,
#     builder_kwargs: Optional[Dict[str, Any]] = None,
#     download_and_prepare_kwargs: Optional[Dict[str, Any]] = None,
#     as_dataset_kwargs: Optional[Dict[str, Any]] = None,
#     try_gcs: bool = False
# )


"""
Example of building dataset:

mnist_builder = tfds.builder("mnist")
mnist_info = mnist_builder.info
mnist_builder.download_and_prepare()
datasets = mnist_builder.as_dataset()
train_dataset, test_dataset = datasets["train"], datasets["test"]
assert isinstance(train_dataset, tf.data.Dataset)
# And then the rest of your input pipeline
train_dataset = train_dataset.repeat().shuffle(1024).batch(128)
train_dataset = train_dataset.prefetch(2)
features = tf.compat.v1.data.make_one_shot_iterator(train_dataset).get_next()
image, label = features['image'], features['label']
print(label)
"""

# dataset = tfds.load('wmt14_translate/de-en',  data_dir=data_dir, split='test', shuffle_files=True, 
#                     # builder_kwargs = {
#                     #     "config": config, 
#                     # }, 
#                     download=False
# )
# # dataset = tfds.load('wmt14_translate/de-en', split='test',shuffle_files=True)
# print(dataset)