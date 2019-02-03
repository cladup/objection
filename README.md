# Mememime
This is an implementation of the [IIIF(International Image Interoperability Framework)](https://iiif.io) specification.
Version: [Image API 2.1](https://iiif.io/api/image/2.1/)

## TODO
* How to truly optimize images/videos/music -> Maybe you could make a compression algorithm lol.
  * Cropping and compression on the fly & CDN stuff.
* Thinking about the processer & resource server.
  * The processer and the server must be not together. They are separate services.
* How does binary data get processed when uploading and downloading in the server & vise versa.
* Storage is a really important factor.
  * How are you going to think about object storage? Compress it and get it?
  * I think compression will be the most important factor over here. 
  * Also getting them ASAP. 
  * Is S3 or Blob storage free in the cloud? If it isn't I have to implement that stuff myself. 
* They call content like images, videos, sound as static content.
  * Can I use NGINX to just serve em?
  * Or should I make an API?
* Asynchronous commitment
  * Actually get images from the storage, but how to make it async.
  * I/O will all be async. Including database queries and storage queries.
  * The problem is, how to find the right implementation for async libraries.
    * This is a tough question. You might not need async in this stuff. 
    * How to make I/O on disk async? Doesn't it just stop everything?
    * If you put the stuff up on like S3 or something, I think it won't be a big deal.

## Development Stack
* I did think about Golang, but I'm going to use Python for fast implementation.
  * Because of concurrency! I also heard that this kid was great at processing this kind of stuff.
    * This statement only goes with golang. But I have to find a way with Python
  * Make a concurrent server, and also split it with CQRS.
* Need more thinking about storage. How to actually store all the objects.
  * Is there a great database that stores blob data? Or is S3 just the way to go.
  * Also, I need to think whether to use a RDBMS or NoSQL db for aliasing.
  * Not sure whether that needs any of relationships.

# License
MIT
