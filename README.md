# Mememime
This project will be a generified image processing server. Planning to make this server able to process images on the fly, and even make a bulk upload client. Hope this project makes a lot of developers live's better!

## TODO
* How to truly optimize images/videos/music -> Maybe you could make a compression algorithm lol.
  * Cropping and compression on the fly & CDN stuff.
  * On what condition to crop?
* Thinking about the processer & resource server.
  * The processer and the server must be not together. They are separate services.
* How does binary data get processed when uploading and downloading in the server & vise versa.
* Storage is a really important factor.
  * How are you going to think about object storage? Compress it and get it?
  * I think compression will be the most important factor over here. 
  * Also getting them ASAP. 
  * Is S3 or Blob storage free in the cloud? If it isn't I have to implement that stuff myself. 
