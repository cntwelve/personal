name := "Chisel3Example2"

version := "0.1"

scalaVersion := "2.12.6"

libraryDependencies += "edu.berkeley.cs" %% "chisel3" % "3.1.0"

scalacOptions ++= Seq("-Xsource:2.11", "-feature", "-language:reflectiveCalls")