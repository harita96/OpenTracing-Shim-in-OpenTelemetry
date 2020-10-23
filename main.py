import time

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.opentracing_shim import create_tracer

# Define which OpenTelemetry Tracer provider implementation to use.
trace.set_tracer_provider(TracerProvider())

# Create an OpenTelemetry Tracer.
otel_tracer = trace.get_tracer(__name__)

# Create an OpenTracing shim.
shim = create_tracer(otel_tracer)

with shim.start_active_span("ProcessHTTPRequest"):
  print("Processing HTTP request")
  # Sleeping to mock real work.
  time.sleep(0.1)
  with shim.start_active_span("GetDataFromDB"):
    print("Getting data from DB")
    # Sleeping to mock real work.
    time.sleep(0.2)