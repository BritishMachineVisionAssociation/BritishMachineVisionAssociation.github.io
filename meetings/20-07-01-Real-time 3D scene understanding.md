---
layout: meeting
type: One Day Meeting
title: "Real-time 3D scene understanding. (1st July 2020)"
index: 1
date: 2020-07-01
meeting-title: "Real-time 3D scene understanding"
image: 20-07-01_SceneUnderstanding.png
organisers: Mihai Bujanca (Manchester University) Horia Porav (University of Oxford)
---

## Keynote Speaker
Andrew Davison (Imperial College London) & Davide Scaramuzza (University of Zurich)


## Call for Papers

In 2015, a BMVA meeting named “Real-time 3D scene understanding in year 2020“ took place.  Tremendous efforts have been devoted to 3D scene understanding over the last decade. Due to their success, a broad range of critical applications like 3D navigation, home robotics, and virtual/augmented reality have been made possible already or are within reach. These applications have drawn the attention and increased aspirations of researchers from the field of computer vision, computer graphics, and robotics. 
This meeting will look at the various aspects of 3D scene understanding, from reconstruction and parsing of 3D scenes, to interaction, data representation, and modelling agents in the scene. Starting from the predictions made in the 2015 meeting, we will look at the past, present, and future of 3D scene understanding. The discussion will be focused around the most promising research directions, and what the state-of-the-art might be in 2025.

A copy of the Call for Papers can be found [here]({{ site.baseurl }}{% link assets/events/20-07-1Call.pdf %}).


## Submission Deadline 

We wish to encourage submissions from students as well as academic and industry researchers in the area. Abstracts are not published and re-presentation of previous work is acceptable.


## Meeting Location

The BCS has moved, the meeting will take place at:

British Computer Society (BCS), 25 Copthall Avenue, London EC2R 7BP

{% include bcs-map.html %}

## Registration

<div class="container-fluid pb-3">
    <div class="card p-1" style="background: #F8F7FA">
        <div class="card-body mx-auto">
          Please register using the options below (scroll for more options):
        </div>
        <div id="eventbrite-widget-container-91995660497"></div>
    </div>
</div>

<script src="https://www.eventbrite.co.uk/static/widgets/eb_widgets.js"></script>

<script type="text/javascript">
    var exampleCallback = function() {
        console.log('Order complete!');
    };

    function getWidth() {
      if (self.innerWidth) {
        return self.innerWidth;
      }

      if (document.documentElement && document.documentElement.clientWidth) {
        return document.documentElement.clientWidth;
      }

      if (document.body) {
        return document.body.clientWidth;
      }
    }

    var height_to_use = 600;

    if (getWidth() < 1000) {
        height_to_use = 650;
    }

    if (getWidth() < 800) {
        height_to_use = 700;
    }

    if (getWidth() < 550) {
        height_to_use = 710;
    }

    window.EBWidgets.createWidget({
        // Required
        widgetType: 'checkout',
        eventId: '91995660497',
        iframeContainerId: 'eventbrite-widget-container-91995660497',

        // Optional
        iframeContainerHeight: height_to_use,  // Widget height in pixels. Defaults to a minimum of 425px if not provided
        onOrderComplete: exampleCallback  // Method called when an order has successfully completed
    });
</script>
Register for a ticket here [here](<https://www.eventbrite.co.uk/e/bmva-symposium-localization-and-spatial-awareness-in-computer-vision-registration-91995660497>)