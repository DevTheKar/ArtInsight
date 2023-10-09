## Inspiration
Hey there, have you ever wondered about the impact of AI-powered art technologies like Dall-E and Midjourney on the world of art? It's fascinating, but it's also sparking a big debate. Some folks are excited, thinking AI will supercharge creativity by making the creative process smoother. But there's another side to the story—some folks worry that AI might take away from the value of art, the blood, sweat, and tears that traditional artists pour into their work. I mean, if anyone can whip up art with a few clicks, what happens to the hardworking artists, right?

Our inspiration for this project came from two very different places. First, we thought about two big themes: Mental Health and Environmental Adaptability. You know when you think about saving the environment, the first thing that pops into your head is probably trees, right? They give us oxygen, after all. But guess what? We're chopping down around 41 million trees every single day just to make paper. That's a lot of trees.

Then, during an amazing trip to Europe, something else caught our attention. We visited seven countries, fifteen cities, and eighteen art museums. It was incredible, but there was a problem. Most of these museums relied on old-school paper pamphlets to tell you about the art. They lacked the juicy details about the artists and their masterpieces.

Take, for instance, the famous Louvre Museum, home to the one and only Mona Lisa. They see about 30,000 visitors a day, and most of them come in pairs. So, you can imagine the number of pamphlets needed! But here's the kicker—most of those pamphlets end up in the trash after the museum visit, not even getting recycled. Now think about all the museums in the world—around 104,000 of them. If they all use pamphlets, that's about 1.5 billion pamphlets wasted every year!

So, what did we do? Well, we decided to step in and create something special—a way to use AI to protect and respect the traditional art that we all hold dear.

## What it does
Meet ArtInsight In response to these problems, we bring you ArtInsight, a web app that's going to change how you experience art. It's simple: just scan any artwork, and ArtInsight will recognize it and give you all the juicy details you crave. We used Python as our trusty tool and got a helping hand from Roboflow to label our images. Plus, we trained our AI with the YOLO version 8 object detection model. But that's not all. ArtInsight has the potential to make museum visits even more awesome. Imagine being able to track all the artworks you've seen and discover new ones you've yet to explore. We're even planning to add a cool MAP feature, so you can navigate the museum like a pro. Not only does ArtInsight deepen your connection with art, but it also helps museums save money by cutting down on pamphlet production. And let's not forget—it's good for the planet too, by saving those precious trees from the chopping block. So, if you're ready to rediscover art in a whole new way, ArtInsight is here to show you the ropes.

## How we built it
We developed these Streamlit apps for object detection using YOLO. Users can upload images, and the apps, powered by pre-trained models, detect objects and provide information about the artists associated with them. They offer straightforward interfaces with options to upload images, use webcams, or provide image URLs. The layouts display the original images and the images with detected objects side by side. Additionally, they link the artists' names to their respective websites, allowing users to explore the art world. These apps offer engaging and educational experiences, bridging the gap between technology and art in user-friendly ways.

## Challenges we ran into
We ran into different challenges as we have never used a machine learning model and also never trained one on custom dataset. When collecting the data, we had to go to the USF contemporary Art Museum which has limited open hours on the weekend. Second challenge was that we believed that we could update the learning model by keep adding images, but what we didn't realize was how long it takes to train a model to be accurate. Another challenge was that the web development experience we have was HTML, CSS, JS, and React for Frontend whereas Django and MySQL for backend. We had never used Streamlit and we didn't even know how to run a machine learning model through the website. Luckily, we were able to figure that out near the end.

## Accomplishments that we're proud of
There is not enough space for us to write the accomplishments we are proud of. The whole Process was a huge challenge and we felt like quitting multiple times. Nevertheless, we finally pulled through it and have a presentable product.

## What we learned
Image Labeling using Roboflow
Training a machine learning model using custom dataset
Gathering custom data
Developing a frontend with Python module Streamlit
What's next for ArtInsight
ArtInsight has the potential to make museum visits even more awesome. Imagine being able to track all the artworks you've seen and discover new ones you've yet to explore. We're even planning to add a cool MAP feature, so you can navigate the museum like a pro.
