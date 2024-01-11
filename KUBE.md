
## About ETCD
kv store + Raft consensus algorithm
- contains: state, configuration, meta data
- [master node], [leader node] (authorized to respond to requests)
- incase of master node failure, a new leader is elected
- watch function keeps config & state in sync 
- 

## Some stuffs about pods
- 3 control nodes preferably
- applying any .yaml -> reflects on etcd -> other components make sure the desired state to match the actual state
- scheduler chooses the node for workloads, create compute
- controller manager [replication manager] recreates failed pods
- [[[pods] deployment] service] you can expose it as loadbalancer

## K8 operators
- k8 control loop - observes state [diff resolving]
- so instead of changing depoyments everytime [config change, scale]
- create operator [from operator hub]
    - has a OLM -> operator lifecycle manager 
    - we define CRD [custom resorce definition] [kind: whatevernameyouwant] + has Controller loop
    - operator STK
- use helm
- #5th maturity - AutoPilot - for auto scaling


## Resources
- https://m.youtube.com/watch?v=OmphHSaO1sE 
- https://m.youtube.com/watch?v=BgrQ16r84pM
- https://m.youtube.com/watch?v=aSrqRSk43lY
- https://m.youtube.com/watch?v=i9V4oCa5f9I
- https://www.ibm.com/topics/etcd#:~:text=the%20next%20step-,What%20is%20etcd%3F,the%20popular%20container%20orchestration%20platform.

## Conserns
- https://www.reddit.com/r/kubernetes/comments/ewkqqw/why_does_k8s_use_etcd/
- Get data by field name (key: field)

