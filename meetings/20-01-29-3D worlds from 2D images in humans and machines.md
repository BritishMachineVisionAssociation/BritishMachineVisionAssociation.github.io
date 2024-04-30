---
layout: meeting
type: One Day Meeting
title: "3D worlds from 2D images in humans and machines. (29th January 2020)"
index: 1
date: 2020-01-29
meeting-title: "3D worlds from 2D images in humans and machines."
image: 20-01-29 3DFrom2D.png
organisers: Andrew Schofield, Aston University. Richard Bowden, University of Surrey. Wendy Adams University of Southampton.
---

## Keynote Speaker

James Elder. Professor of Human and Computer Vision, York University, Toronto.
Johannes Burge, University of Pennsylvania
Lourdes Agapito, University College London.

## Videos of Talks

On our BMVA YouTube channel there are recorded talks of the slides and speaker from the day [here](https://www.youtube.com/playlist?list=PLW8VWHVjepIsuKddDZmImJJ2vAqDcBQNO)

<div class="container">
	<div class="row"><div class="col-xs-12 col-lg-10 mx-auto">
		<div class="video-container">
			<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLW8VWHVjepIsuKddDZmImJJ2vAqDcBQNO " frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
		</div>
	</div></div>
</div>

## Programme

When humans view a photograph they perceive the 3D world that constructed the image. They can, for example, describe the depth relationships between objects, plan a route through the scene and imagine the scene from a different viewpoint. This process is automatic and compulsive. For example, even though humans possess size constancy they will readily misinterpret the size of a person in order to make sense of the rest of the scene as a 3D world.  State of the art computer vision systems are now also very good at reconstructing 3D layout from 2D images (3D uplift) although, unlike humans, this is often restricted to specific domains or requires multiple views. This workshop will consider recent developments in 3D uplift as well as our current knowledge of scene understanding in human vision.

10:00 - Registration and Coffee

10:30 - **Andrew Schofield,** Aston University, Welcome and Introduction

10:35 - **Wendy Adams,** University of Southampton, The Southampton & York Natural image Dataset

10:45 - **Keynote talk James Elder,** York University, Canada

11:30 - **Rebecca Lawson**, University of Liverpool, Size perception for real, 3D objects and for 2D images on a specified plane

11:50 - **Paul Linton,** City, University of London, Does Human Vision Triangulate Absolute Distance?

12:10 - **Brian Rogers,** University of Oxford, 3D worlds from 2D images: a mistaken conception

12:30 Lunch

13:30 - **Keynote talk Johannes Burge,** University of Pennsylvania

14:20 - **Dhanraj Vishwanath,** University of St Andrews, What constitutes the perception of pictorial depth?

14:40 - **Robert Black,** RealSpace, ‘Paradoxical’ Bi-Ocular Stereoscopy - 25 years on

15:00 – Coffee

15:20 **Keynote talk Lourdes Agapito,** University College London.

16:10 **Will Smith,** University of York, Self-supervised shape from shading and inverse rendering in the wild  

16:30 **Oisin Mac Aodha,** University of Edinburgh, Digging into Monocular Depth Estimation


A copy of the Programme can be found [here]({{ site.baseurl }}{% link assets/events/20-01-29Programme.pdf %}).

## Meeting Location

The BCS  moved in September, the meeting will take place at:

British Computer Society (BCS), 25 Copthall Avenue, London EC2R 7BP

{% include bcs-map.html %}

<!---
The Programme can be downloaded from [here]({{ site.baseurl }}{% link assets/events/19-09-25Programme.pdf %}).
--->

<!---
## Videos of Talks
On our BMVA youtube channel there are recorded talks of the slides and speaker from the day [here](https://www.youtube.com/playlist?list=PLW8VWHVjepIsW0S7K_ozIOS4_DGy0qoJf)
<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLW8VWHVjepIsW0S7K_ozIOS4_DGy0qoJf" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Meeting Report
After the meeting the organisers will preapre a short summary of the meeting. 

This can be found [here]({{ site.baseurl }}{% link assets/events/bmvameetingreport-19-02-20.pdf %}).
--->

## Registration

<div class="container-fluid pb-3">
    <div class="card p-1" style="background: #F8F7FA">
        <div class="card-body mx-auto">
          Please register using the options below (scroll for more options):
        </div>
        <div id="eventbrite-widget-container-77113995035"></div>
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
        eventId: '77113995035',
        iframeContainerId: 'eventbrite-widget-container-77113995035',

        // Optional
        iframeContainerHeight: height_to_use,  // Widget height in pixels. Defaults to a minimum of 425px if not provided
        onOrderComplete: exampleCallback  // Method called when an order has successfully completed
    });
</script>
