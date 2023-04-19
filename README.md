# chanloader 
you love [4chan](https://www.4chan.org)? but gotta download each file with so many clicks? nahhhh...<br>
[chanloader](https://github.com/eawlot3000/chanloader) is a tool that help you download all the visual content of your fond channels on 4chan

# features
* **Multithreading?** speed up bro
* support multi-thread urls in single run
* save all downloaded to a new local folder! you name it!
* display each [filename] and [filesize]
* `WARNING` with too many requests


# requirements
```bash
pip install -r requirements.txt
```

# usage
#### (with instructions) with channel, single run:
```
python main.py
```

#### (with instructions) with threads
```
python thread.py
```


----

```
├── LICENSE
├── README.md
├── function // for work only
├── main.py
├── requirements.txt
└── thread // thread support!
    ├── test.py
    └── thread.py // `use this bro`
```

# `TODO`
* improve main, include thread to do multi pages works!
* /* {feature: parse one channel url and then mass download all threads!} */

