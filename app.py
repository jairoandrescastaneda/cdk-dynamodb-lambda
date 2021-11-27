#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from aws_cdk import core

from myproject.mystack import MyProjectStack


app = core.App()
MyProjectStack(app, "MyprojectStack")

app.synth()
