import math

def generate_fee(duration, fees):
    return fees[1] + (math.ceil((duration - fees[0]) / fees[2]) * fees[3] if duration > fees[0] else 0)

def solution(fees, records):
    record_hash = {}
    fee_hash = {}
    
    for record in records:
        time, car, io = record.split()
        hour, minute = map(int, time.split(":"))
        
        time = hour * 60 + minute
        car = int(car)
        
        if io == "IN":
            record_hash[car] = time
            fee_hash.setdefault(car, 0)
                
        if io == "OUT":
            fee_hash[car] += time - record_hash[car]
            record_hash.pop(car, None)
        
            
    for record in record_hash:
        time = (23 * 60 + 59)
        fee_hash[record] += time - record_hash[record]
    
    for fee in fee_hash:
        fee_hash[fee] = generate_fee(fee_hash[fee], fees)
        
    
    return [fee_hash[key] for key in sorted(fee_hash)]