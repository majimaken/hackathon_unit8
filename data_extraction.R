production_line_optimization_first_log <- read_delim("Task/production_line_optimization_first_log.csv", delim = ";")
timestamp_raw <- as.data.frame(production_line_optimization_first_log)
str(timestamp_raw)
names(timestamp_raw)[1] <- "ID" 

as.integer(difftime(timestamp_raw$time[2], timestamp_raw$time[1], units = "secs"))

timestamp_A <- timestamp_raw[timestamp_raw$line == "A",]

timestamp_A1 <- timestamp_A[timestamp_A$module == 1,]
timestamp_A2 <- timestamp_A[timestamp_A$module == 2,]
timestamp_A3 <- timestamp_A[timestamp_A$module == 3,]


getTimes <-function(timestamp_Line_Module){
  data <- data.frame(job_id=0, time=0)
  for (job_id in min(timestamp_Line_Module$job_id):max(timestamp_Line_Module$job_id)) {
    timestamp_Line_Module_Job <- timestamp_Line_Module[timestamp_Line_Module$job_id==job_id,]
    diff <- as.integer(difftime(timestamp_Line_Module_Job[timestamp_Line_Module_Job$state=="storing_job","time"],
                                timestamp_Line_Module_Job[timestamp_Line_Module_Job$state=="fetching_job","time"], units = "secs"))
    data[job_id,] <- c(job_id, diff[1])
  }
  return(data)
}


getTimesLast <-function(timestamp_Line_Module){
  data <- data.frame(job_id=0, time=0)
  for (job_id in min(timestamp_Line_Module$job_id):(max(timestamp_Line_Module$job_id)-1)) {
    timestamp_Line_Module_Job <- timestamp_Line_Module[timestamp_Line_Module$job_id==job_id,]
    timestamp_Line_Module_Job_next <- timestamp_Line_Module[timestamp_Line_Module$job_id==(job_id+1),] 
    diff <- as.integer(difftime(timestamp_Line_Module_Job_next[timestamp_Line_Module_Job$state=="fetching_job","time"],
                                timestamp_Line_Module_Job[timestamp_Line_Module_Job$state=="fetching_job","time"], units = "secs"))
    data[job_id,] <- c(job_id, diff[1])
  }
  data[max(timestamp_Line_Module$job_id),] <- c(max(timestamp_Line_Module$job_id), as.integer(mean(data$time)))
  return(data)
}

getTimes(timestamp_A1)
getTimes(timestamp_A2)
getTimesLast(timestamp_A3)

data

