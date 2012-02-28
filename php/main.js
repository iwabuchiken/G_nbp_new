//version
//created_at
//project
function get_time_label(){
    var label = "";
    time_label_s = new Array();
    now = new Date();
    time_label = new Array();
    time_label.push(now.getFullYear());
    time_label.push(now.getMonth());
    time_label.push(now.getDate());
    time_label.push(now.getHours());
    time_label.push(now.getMinutes());
    time_label.push(now.getSeconds());

    for (i = 0; i < time_label.length; i = i + 1){
//      if (i < 3) {
        time_label[i] = "" + time_label[i];
        if (time_label[i].length < 2){time_label[i] = "0" + time_label[i];}
        time_label_s.push(time_label[i]);
//      }
    }

    return time_label_s.slice(0, 3).join("") + "_" +
              time_label_s.slice(3, time_label_s.lenth).join("");

//    return time_label[1,2]
//    return time_label
}
