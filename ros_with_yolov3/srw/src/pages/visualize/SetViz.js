import React, { useState } from "react";
import ROSLIB from "roslib";
import VizStyles from "./VizStyles";
import { CardMedia,Grid} from "@material-ui/core";

const ros = new ROSLIB.Ros({ url: "ws://localhost:9090" });

const cam0Topic = new ROSLIB.Topic({
  ros: ros,
  name: "/test/cam/compressed",
  messageType: "sensor_msgs/CompressedImage",
});

const detectionTopic = new ROSLIB.Topic({
  ros: ros,
  name: "/darknet_ros/detection_image/compressed",
  messageType: "sensor_msgs/CompressedImage",
});


const doCaptureTopic = new ROSLIB.Topic({
  ros: ros,
  name: "/test/web/do_capture",
  messageType: "std_msgs/Int8",
});

const SetViz = (props) => {
  const classes = VizStyles();
  const [receiveCam0, setReceiveCam0] = useState([]);
  const [receiveDetection, setReceiveDetection] = useState([]); 
  const [isSub, setIsSub] = useState(false);

  if (!isSub && props.sub) {
    setIsSub(true);
    cam0Topic.subscribe(function (message) {
      let image = new Image();
      image.src = "data:image/jpg;base64," + message.data;
      setReceiveCam0(image);
    });
    detectionTopic.subscribe(function (message) {
      let image = new Image();
      image.src = "data:image/jpg;base64," + message.data;
      setReceiveDetection(image);
    });
  }

  const doCaptureCam = () => {
    if (isSub) {
      doCaptureTopic.publish({ data: 1 });
    }
  }

  const doCaptureDetection = () => {
    if (isSub) {
      doCaptureTopic.publish({ data: 2 });
    }
  }

  if (isSub && !props.sub) {
    setIsSub(false);
    cam0Topic.unsubscribe();
    detectionTopic.unsubscribe();
  }

  return (
    <Grid container spacing={2}>
      <Grid item lg={6}>
        <CardMedia
          onClick={doCaptureCam}
          component="img"
          className={classes.media}
          image={receiveCam0.src}
        />
      </Grid>
      <Grid item lg={6}>
      <CardMedia
        onClick={doCaptureDetection}
        component="img"
        className={classes.media}
        image={receiveDetection.src}
      />
      </Grid>
    </Grid>     
  );
};

export default SetViz;